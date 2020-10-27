from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
# this is a show text - hide text situation
# this selenium code only run when the textbox i.e. displayed-text is in html code
assert driver.find_element_by_id("displayed-text").is_displayed()  # is_displayed() returns true (show text) / false
# (hide text)
# assert to check if return true or not

driver.find_element_by_id("hide-textbox").click()  # clicking on hide button

assert not driver.find_element_by_id("displayed-text").is_displayed()
# assert not to check if return true i.e is_displayed() returns false or not

