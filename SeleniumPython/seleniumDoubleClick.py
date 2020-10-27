from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")

# for any mouse driven work in web pages like double click, mouse over etc ActionChains class is to be imported
# in ActionChains class driver object should be given as an argument to pass it to the object objAction
objAction = ActionChains(driver)

doubleClick = driver.find_element_by_css_selector("#double-click")

# perform() method to be added any ActionChains class, otherwise no action will happen
objAction.context_click(doubleClick).perform()  # context_click() means right click in mouse
objAction.double_click(doubleClick).perform()  # double_click() means double click in mouse

goAlert = driver.switch_to.alert
goAlert.accept()


