# This is a Python script for Shortlyster CV upload automation.
# This is a Python script for Shortlyster CV upload automation.

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager import driver

from utilities import webdriver_load, upload_CV_prefilled_disabled, upload_CV_prefilled_enabled,is_element_exist

#assert isinstance(webdriver_load(), object) #  declared in login

webdriver_load()
assert is_element_exist("WRONG EMAIL OR PASSWORD") == "False" # verify if the login was successful.

#upload_CV_prefilled_enabled() # this function will upload the CV




