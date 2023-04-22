from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time

chromedriver_autoinstaller.install()
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(service=Service(), options=options)

driver.maximize_window()
driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(5)

language = driver.find_element(By.ID, 'langSelect-EN')
language.click()

time.sleep(5)

cookie = driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split()[0].replace(',', '')
while int(cookie) < 999999:
    button_click = driver.find_element(By.ID, 'bigCookie')
    button_click.click()
    if int(cookie) > int(driver.find_element(By.XPATH, '//*[@id="productPrice0"]').text.split()[0].replace(',', '')):
        first_up = driver.find_element(By.XPATH, '//*[@id="product0"]')
        first_up.click()
    elif int(cookie) > int(driver.find_element(By.XPATH, '//*[@id="productPrice1"]').text.split()[0].replace(',', '')):
        second_up = driver.find_element(By.XPATH, '//*[@id="product1"]')
        second_up.click()
    elif int(cookie) > 1100:
        if int(cookie) > int(driver.find_element(By.XPATH, '//*[@id="productPrice2"]').text.split()[0].replace(',', '')):
            third_up = driver.find_element(By.XPATH, '//*[@id="product2"]')
            third_up.click()
    elif int(cookie) > 12000:
        if int(cookie) > int(driver.find_element(By.XPATH, '//*[@id="productPrice3"]').text.split()[0].replace(',', '')):
            fourth_up = driver.find_element(By.XPATH, '//*[@id="product3"]')
            fourth_up.click()
    elif int(cookie) > 180000:
        if int(cookie) > int(driver.find_element(By.XPATH, '//*[@id="productPrice4"]').text.split()[0].replace(',', '')):
            fourth_up = driver.find_element(By.XPATH, '//*[@id="product4"]')
            fourth_up.click()
    cookie = driver.find_element(By.XPATH, '//*[@id="cookies"]').text.split()[0].replace(',', '')
