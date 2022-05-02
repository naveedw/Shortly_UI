# This is a Python script for Shortlyster CV upload automation.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
from webbrowser import Chrome
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager import driver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, wait
from selenium.common.exceptions import NoSuchElementException
import os

def webdriver_load():
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")

    chrome_options.add_argument('start-maximized')
    chrome_options.add_experimental_option('useAutomationExtension', False)
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument('--disable-blink-features=AutomationControlled')
    chrome_options.add_argument('--start-maximized')
    chrome_options.add_argument('--disable-infobars')

    ser = Service("C:\DRIVERS\chromedriver_win32\chromedriver.exe")
    # driver = webdriver.Chrome(options=chrome_options, executable_path=r"C:\DRIVERS\chromedriver_win32\chromedriver.exe")
    driver = webdriver.Chrome(service=ser, options=chrome_options, executable_path=ser)

    # yield driver  #return the browser object in case other tests wants to call it.
    driver.get("https://candidate--qa-exercise-april.reviews.compono.dev/signup")
    wait = WebDriverWait(driver, 10)

    username = wait.until(EC.element_to_be_clickable((By.ID, '1-email')))
    username.click()
    username.send_keys('waqas.naveed@gmail.com')
    password_field = wait.until(EC.element_to_be_clickable((By.NAME, 'password')))
    password_field.click()
    password_field.send_keys('@Shortly@123')
    # wait
    # username = driver.find_element_by_xpath('//*[@id="1-email"]')
    # password = driver.find_element_by_xpath('//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/input')
    #
    # username.click()
    # username.send_keys("waqas.naveed@gmail.com")
    # password.click()
    # password.send_keys("@Shortly@123")

    loginButton = driver.find_element_by_xpath('//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button')
    loginButton = driver.find_element(by=By.XPATH,value='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button')
    loginButton.click()

    # try:
    #     element = driver.find_element_by_partial_link_text("WRONG EMAIL OR PASSWORD.")
    # except NoSuchElementException:
    #     print("No element found")


def is_element_exist(text):
    try:
        # validationText = wait.until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, text)))
        # '//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[1]/div/div'
        validationText = driver.find_element(by=By.XPATH,value='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[1]/div/div/span/span'.getText())
        assert validationText == text
    except TimeoutException:
        return False


def upload_CV_prefilled_disabled():
    driver.find_element(By.CSS_SELECTOR,
                        ".Wrapper-sc-9s5zbo-1:nth-child(2) .Switcheroo-ut0ai-0").click()  # to disable the  profile pre-fill
    driver.find_element(By.CSS_SELECTOR, "#cv > .css-130mppw").click()  # upload your cv button from profile
    driver.find_element(By.CSS_SELECTOR, ".css-130mppw:nth-child(1)").click()  # upload your CV from pop-up
    driver.find_element(By.ID, "cv-upload-*").send_keys(
        "D:\\Documents\\Waqas\\Resume\\Shortlyster\\Scenario1.docx")  # '//*input[@id="cv-upload-kclxdn"]'
    driver.find_element(By.CSS_SELECTOR, ".CloseIconButton-sc-19wgu2s-0").click()


def upload_CV_prefilled_enabled():
    driver.find_element(By.CSS_SELECTOR, "#cv > .css-130mppw").click()  # upload your cv button from profile
    driver.find_element(By.CSS_SELECTOR, ".css-130mppw:nth-child(1)").click()  # upload your CV from pop-up
    driver.find_element(By.ID, "cv-upload-*").send_keys("D:\\Documents\\Waqas\\Resume\\Shortlyster\\Scenario1.docx")
    driver.find_element(By.CSS_SELECTOR, ".CloseIconButton-sc-19wgu2s-0").click()

# this is to check if the respective directory has the CVs in place
def check_cv(path: str):
  path = path
  dir = os.listdir(path)
  files = len(dir)
  f"the word file in the respective directory are: {files}"
  return files