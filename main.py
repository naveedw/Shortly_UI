# This is a Python script for Shortlyster CV upload automation.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from time import sleep
from webbrowser import Chrome

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

ser = Service("C:\DRIVERS\chromedriver_win32\chromedriver.exe")
# https://stackoverflow.com/questions/29858752/error-message-chromedriver-executable-needs-to-be-available-in-the-path
chrome_options = webdriver.chrome.options.Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--incognito")

chrome_options.add_argument('start-maximized')
chrome_options.add_experimental_option('useAutomationExtension', False)
chrome_options.add_experimental_option("excludeSwitches",["enable-automation"])
chrome_options.add_argument( '--disable-blink-features=AutomationControlled' )


capabilities = {
  'browserName': 'chrome',
  'chromeOptions':  {
    'useAutomationExtension': False,
    'forceDevToolsScreenshot': True,
    'args': ['--start-maximized', '--disable-infobars']
  }
}



#driver = webdriver.Chrome(options=chrome_options, executable_path=r"C:\DRIVERS\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(service=ser, options=chrome_options,  executable_path=ser, desired_capabilities=capabilities)

driver.get("https://candidate--qa-exercise-april.reviews.compono.dev/signup")
# driver.implicitly_wait(10) # seconds
# delay = 5; #second

# while True:
#     try:
#         WebDriverWait(driver, delay).until(EC.presence_of_element_located(driver.find_element(by=By.XPATH, value='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button')))
#         print("Page is ready!")
#         break # it will break from the loop once the specific element will be present.
#     except TimeoutException:
#         print("Loading took too much time!-Try again")


# loginOption = driver.find_element(by=By.XPATH, value='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[1]/ul/li[1]/a')
# loginOption.click()
#sleep(1000)
#signUpOption = driver.find_element(by=By.XPATH, value='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[1]/ul/li[2]/span')
#signUpOption.click()

wait = WebDriverWait(driver,10)
username = wait.until(EC.element_to_be_clickable((By.ID,'1-email')))
username.click()
username.send_keys('waqas.naveed@gmail.com')
#
# #username = driver.find_element(by=By.XPATH, value='//*[@id="1-email"]')
# #password = driver.find_element(by=By.XPATH, value='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/div/div[2]/div[2]/span/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div/input')
# #username.send_keys("waqas.naveed@gmail.com")
#
password_field = wait.until(EC.element_to_be_clickable((By.NAME,'password')))
password_field.click()
password_field.send_keys('@Shortly@123')
#
# #password.send_keys("@Shortly@123")
#
# #loginButton = driver.find_element_by_xpath('//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button')
# loginButton = driver.find_element(by=By.XPATH, value='//*[@id="auth0-lock-container-1"]/div/div[2]/form/div/div/div/button')
#
# loginButton.click()
#
#
#
# # See PyCharm help at https://www.jetbrains.com/help/pycharm/
