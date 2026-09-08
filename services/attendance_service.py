import time

from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger_config import log_message


class AttendanceService:

    REFRESH_INTERVAL = 300  # 5 минут
    ELEMENT_TIMEOUT = 20

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

    def mark_attendance(self, lesson):
        log_message(f"Начата обработка занятия: {lesson['name']}")

        try:
            self.browser.start()
            self.auth_service.open_schedule()
            driver = self.browser.driver

            while True:
                try:
                    self._find_start_button(driver).click()
                    log_message(
                        f'Поставлена отметка на паре "{lesson["name"]}"'
                    )
                    return
                except TimeoutException:
                    pass

                try:
                    self._find_refresh_button(driver).click()
                except TimeoutException:
                    time.sleep(self.REFRESH_INTERVAL)
                    continue

                try:
                    self._find_start_button(driver).click()
                    log_message(
                        f'Поставлена отметка на паре "{lesson["name"]}"'
                    )
                    return
                except TimeoutException:
                    time.sleep(self.REFRESH_INTERVAL)

        except WebDriverException as exc:
            log_message(f"Ошибка WebDriver при отметке: {exc}")
            raise
        except Exception as exc:
            log_message(f"Ошибка при отметке посещаемости: {exc}")
            raise
        finally:
            self.browser.stop()
