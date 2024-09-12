import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

URL = 'http://hotel-v3.progmasters.hu/'
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--headless')
options.add_argument("--disable-search-engine-choice-screen")
browser = webdriver.Chrome(options=options)

def test_postman_1():
    url = "http://localhost:8080/api/categories"
    payload = {}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    assert response.text == '[{"id":1,"name":"WOODWIND"},{"id":2,"name":"BRASS INSTRUMENTS"},{"id":3,"name":"PERCUSSION INSTRUMENTS"},{"id":4,"name":"KEYBOARD INSTRUMENTS"},{"id":5,"name":"GUITAR FAMILY"},{"id":6,"name":"BOWED STRINGS"},{"id":7,"name":"MISC"},{"id":14,"name":"TRADITIONAL"}]'

def test_postman_user():
    browser.get('https://app.endtest.io/mailbox?email=progmasterstn@endtest-mail.io')
    time.sleep(1)
    browser.refresh()
    last_email = WebDriverWait(browser, 10).until(EC.visibility_of_any_elements_located((By.XPATH, '//div[@class="email_item"]')))[0]
    last_email.click()
    WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.XPATH, '//a[text()="Activate Now"]'))).click()
