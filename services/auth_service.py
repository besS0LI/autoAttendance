import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger_config import log_message


class AuthService:

    def __init__(self, browser, email, password):
        self.browser = browser
        self.email = email
        self.password = password

    def open_schedule(self):
        driver = self.browser.driver

        try:
            log_message("Открываем страницу авторизации")
            driver.get("https://lk.sut.ru/")

            log_message(
                f"URL после открытия: {driver.current_url}"
            )
            log_message(
                f"Title страницы: {driver.title}"
            )

            log_message("Ожидание поля логина")

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, "users"))
            ).send_keys(self.email)

            log_message("Поле логина найдено")

            log_message("Ввод пароля")

            driver.find_element(
                By.ID, "parole"
            ).send_keys(self.password)

            log_message("Нажимаем кнопку входа")

            driver.find_element(
                By.ID, "logButton"
            ).click()

            log_message("Авторизация выполнена")

            log_message("Ожидание элемента title_item")

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "title_item")
                )
            ).click()

            log_message("title_item найден")

            log_message("Ожидание пункта расписания menu_li_6118")

            WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable(
                    (By.ID, "menu_li_6118")
                )
            ).click()

            log_message("Пункт расписания найден")

            time.sleep(3)

            log_message(
                f"Расписание открыто. URL: {driver.current_url}"
            )

        except TimeoutException as exc:
            log_message(
                f"TIMEOUT в AuthService: {type(exc).__name__}"
            )
            log_message(
                f"Текущий URL: {driver.current_url}"
            )
            log_message(
                f"Title: {driver.title}"
            )

            try:
                driver.save_screenshot(
                    "/tmp/autoattendance_error.png"
                )
                log_message(
                    "Screenshot сохранён: "
                    "/tmp/autoattendance_error.png"
                )
            except Exception as screenshot_exc:
                log_message(
                    f"Не удалось сохранить screenshot: "
                    f"{screenshot_exc}"
                )

            raise
