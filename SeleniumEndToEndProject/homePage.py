from selenium import webdriver
from selenium.webdriver.support.select import Select

import time

from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
#driver.maximize_window()

driver.find_element_by_css_selector("[name='name']").send_keys("Chandrika")
driver.find_element_by_name("email").send_keys("chandrika_sen@rediffmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("Sengupta")
driver.find_element_by_id("exampleCheck1").click()

# dropdown locator. for that we have to impot this - from selenium.webdriver.support.select import Select
sel = Select(driver.find_element_by_id("exampleFormControlSelect1"))
sel.select_by_visible_text("Female")

driver.find_element_by_id("inlineRadio2").click()
driver.find_element_by_name("bday").send_keys("08/21/1975")
driver.find_element_by_class_name("btn-success").click()
seccessText = driver.find_element_by_css_selector("[class='alert alert-success alert-dismissible']").text
print(seccessText)
assert "Success" in seccessText


# driver.close()