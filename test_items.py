from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time


def test_lang(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "add_to_basket_form"))
    )
    browser.implicitly_wait(15)
