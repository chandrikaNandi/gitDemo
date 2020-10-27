
from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://login.salesforce.com")

driver.find_element_by_css_selector("#username").send_keys("chandrika")   # CSS locate using web element ID
driver.find_element_by_css_selector(".password").send_keys("nandi")   # CSS locate using web element CLASS

driver.find_element_by_css_selector(".password").clear()

driver.find_element_by_id("rememberUn").click()  # syntax of locators for checkbox

driver.find_element_by_link_text("Use Custom Domain").click()   # syntax of LinkText locator

driver.find_element_by_xpath("//button[text()='Back']").click()    # generating Xpath based on text only. locator can
# locate simple text through Xpath by this syntax. it is not possible in Css

print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)  #syntax for Xpath traversing from grand-
# parent to child path locator

print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)   #syntax for Css traversing
# from grand-parent to child path locator


