from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")  # we have to put frame name or frame id frame list in frame() method

driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("Hi! How are you?")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)

