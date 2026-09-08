import time

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from logger_config import log_message


class AuthService:

    ELEMENT_TIMEOUT = 20

    def __init__(self, browser, email, password):
        self.browser = browser
        self.email = email
        self.password = password

    def open_schedule(self):
        driver = self.browser.driver

        try:
            log_message("Открываем страницу авторизации")
            driver.get("https://lk.sut.ru/")

            WebDriverWait(driver, self.ELEMENT_TIMEOUT).until(
                EC.element_to_be_clickable((By.ID, "users"))
            ).send_keys(self.email)

            driver.find_element(By.ID, "parole").send_keys(self.password)
            driver.find_element(By.ID, "logButton").click()

            WebDriverWait(driver, self.ELEMENT_TIMEOUT).until(
                EC.element_to_be_clickable(
                    (By.CLASS_NAME, "title_item")
                )
            ).click()

            WebDriverWait(driver, self.ELEMENT_TIMEOUT).until(
                EC.element_to_be_clickable(
                    (By.ID, "menu_li_6118")
                )
            ).click()

            time.sleep(3)

        except TimeoutException as exc:
            log_message(
                f"Ошибка ожидания элементов авторизации: {type(exc).__name__}"
            )
            log_message(f"Текущий URL: {driver.current_url}")
            log_message(f"Title: {driver.title}")

            try:
                driver.save_screenshot("/tmp/autoattendance_error.png")
            except Exception:
                pass

            raise
