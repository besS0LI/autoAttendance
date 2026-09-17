import re
import time
from datetime import datetime, timedelta

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger_config import log_message


class AttendanceService:

    REFRESH_INTERVAL = 300  # 5 минут
    ELEMENT_TIMEOUT = 20
    ATTENDANCE_WINDOW = timedelta(hours=1, minutes=35)

    def __init__(self, browser, auth_service):
        self.browser = browser
        self.auth_service = auth_service

    def _find_start_button(self, driver):
        return WebDriverWait(driver, self.ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@onclick, 'open_zan')]")
            )
        )

    def _find_refresh_button(self, driver):
        return WebDriverWait(driver, self.ELEMENT_TIMEOUT).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(@onclick, 'update_zan')]")
            )
        )

    def _get_attendance_span_id(self, button):
        return button.find_element(
            By.XPATH, "./.."
        ).get_attribute("id")

    def _wait_for_attendance_confirmation(self, driver, span_id):
        def is_confirmed(d):
            span = d.find_element(By.ID, span_id)

            return (
                not span.find_elements(By.TAG_NAME, "a")
                and bool(re.fullmatch(r"\d{2}:\d{2}", span.text.strip()))
            )

        WebDriverWait(driver, self.ELEMENT_TIMEOUT).until(is_confirmed)

    def _try_mark_attendance(self, driver, lesson_name):
        button = self._find_start_button(driver)
        span_id = self._get_attendance_span_id(button)

        button.click()

        self._wait_for_attendance_confirmation(driver, span_id)

        log_message(
            f'Отметка подтверждена на паре "{lesson_name}"'
        )
        return True

    def _get_attendance_deadline(self, lesson):
        now = datetime.now()
        lesson_start = datetime.strptime(
            lesson["start_time"], "%H:%M"
        ).replace(
            year=now.year,
            month=now.month,
            day=now.day,
        )
        return lesson_start + self.ATTENDANCE_WINDOW

    def _is_expired(self, deadline, lesson_name):
        if datetime.now() >= deadline:
            log_message(
                f'Время отметки пары "{lesson_name}" истекло. '
                f"Попытки прекращены"
            )
            return True
        return False

    def _sleep_until_retry(self, deadline):
        remaining = (deadline - datetime.now()).total_seconds()
        if remaining <= 0:
            return
        time.sleep(min(self.REFRESH_INTERVAL, remaining))

    def mark_attendance(self, lesson):
        lesson_name = lesson["name"]
        deadline = self._get_attendance_deadline(lesson)

        log_message(f"Начата обработка занятия: {lesson_name}")

        try:
            self.browser.start()
            self.auth_service.open_schedule()
            driver = self.browser.driver

            while not self._is_expired(deadline, lesson_name):
                try:
                    self._try_mark_attendance(
                        driver,
                        lesson_name,
                    )
                    return True
                except TimeoutException:
                    log_message(
                        f'Отметка на паре "{lesson_name}" '
                        f"не подтверждена"
                    )

                if self._is_expired(deadline, lesson_name):
                    return False

                try:
                    self._find_refresh_button(driver).click()
                except TimeoutException:
                    self._sleep_until_retry(deadline)
                    continue

                if self._is_expired(deadline, lesson_name):
                    return False

                try:
                    self._try_mark_attendance(
                        driver,
                        lesson_name,
                    )
                    return True
                except TimeoutException:
                    log_message(
                        f'Отметка на паре "{lesson_name}" '
                        f"не подтверждена после обновления"
                    )
                    self._sleep_until_retry(deadline)

            return False

        except WebDriverException as exc:
            log_message(f"Ошибка WebDriver при отметке: {exc}")
            raise
        except Exception as exc:
            log_message(f"Ошибка при отметке посещаемости: {exc}")
            raise
        finally:
            self.browser.stop()
