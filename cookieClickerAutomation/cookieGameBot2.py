from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import datetime

chrome_driver_path = "/Users/a65911/Downloads/chromedriver"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

url = "http://orteil.dashnet.org/experiments/cookie/"
driver.get(url)

cookie_button = driver.find_element(By.XPATH, '//*[@id="cookie"]')


# print(cookie_button)

def check_prices():
    # Extracting relevant values
    current_number_of_cookies = int(driver.find_element(By.XPATH, '//*[@id="money"]').text.replace(",", ""))
    cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]')
    grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]')
    factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]')
    mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]')
    shipment = driver.find_element(By.XPATH, '//*[@id="buyShipment"]')
    alchemy_lab = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]')
    portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]')
    time_machine = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]')

    cursor_price = int(driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.split()[-1].replace(",", ""))
    grandma_price = int(driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.split()[-1].replace(",", ""))
    factory_price = int(driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.split()[-1].replace(",", ""))
    mine_price = int(driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.split()[-1].replace(",", ""))
    shipment_price = int(driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text.split()[-1].replace(",", ""))
    alchemy_lab_price = int(
        driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.split()[-1].replace(",", ""))
    portal_price = int(driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b').text.split()[-1].replace(",", ""))
    time_machine_price = int(
        driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.split()[-1].replace(",", ""))
    if current_number_of_cookies >= time_machine_price:
        time_machine.click()
    elif current_number_of_cookies >= portal_price:
        portal.click()
    elif current_number_of_cookies >= alchemy_lab_price:
        alchemy_lab.click()
    elif current_number_of_cookies >= shipment_price:
        shipment.click()
    elif current_number_of_cookies >= mine_price:
        mine.click()
    elif current_number_of_cookies >= factory_price:
        factory.click()
    elif current_number_of_cookies >= grandma_price:
        grandma.click()
    elif current_number_of_cookies >= cursor_price:
        cursor.click()


def game_continues():
    timeout = datetime.timedelta(minutes=5)  # 300s from now
    timeout_start = datetime.datetime.now()
    lastrun = datetime.datetime.now()
    iteration_time = datetime.timedelta(seconds=5)

    while datetime.datetime.now() < timeout_start + timeout:
        cookie_button.click()
        now = datetime.datetime.now()
        if now >= lastrun + iteration_time:
            check_prices()
            lastrun = datetime.datetime.now()


game_continues()
driver.quit()
