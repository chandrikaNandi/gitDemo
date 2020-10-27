from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element_by_link_text("Click Here").click()

childWindow = driver.window_handles[1]  # It takes the ID of child window, for parent window_handles[0]

driver.switch_to.window(childWindow)   # we have to pass the ID of the window in switch_to.window(ID) method

print(driver.find_element_by_tag_name("h3").text)

driver.close()  # close current window that is child window

driver.switch_to.window(driver.window_handles[0])  # back to parent window

print(driver.find_element_by_tag_name("h3").text)
