from django.test import TestCase
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
# Create your tests here.

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.get(url='http://127.0.0.1:8000/admin')

def add_random_post():
    driver.find_element('xpath','//*[@id="id_username"]').send_keys('admin')
    driver.find_element('xpath','//*[@id="id_password"]').send_keys('admin')
    time.sleep(1)
    driver.find_element('xpath','//*[@id="login-form"]/div[3]/input').click()
    time.sleep(1)
    driver.find_element('xpath','//*[@id="user-tools"]/a[1]').click()
    time.sleep(1)
    driver.find_element('xpath','/html/body/nav/div/a').click()
    time.sleep(1)
    driver.find_element('xpath','//*[@id="id_title"]').send_keys('Test Title')
    driver.find_element('xpath','//*[@id="id_text"]').send_keys('Test Text')
    driver.find_element('xpath','/html/body/div[1]/div/div/div/form/button').click()

def respons_check(w, file):
    height = 768
    driver.set_window_size(w, height)
    driver.save_screenshot(file)

respons_check(600, 'test600.png')
respons_check(900, 'test900.png')
respons_check(1200, 'test1200.png')
respons_check(1800, 'test1800.png')
