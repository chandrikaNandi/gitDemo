from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# for any mouse driven work in web pages like double click, mouse over etc ActionChains class is to be imported
# in ActionChains class driver object should be given as an argument to pass it to the object objAction
objAction = ActionChains(driver)

mouseOverMenu = driver.find_element_by_css_selector("#mousehover")

objAction.move_to_element(mouseOverMenu).perform()  # perform() method to be added any ActionChains class,
# otherwise no action will happen

mouseOverClick = driver.find_element_by_link_text("Top")

objAction.move_to_element(mouseOverClick).click().perform()
