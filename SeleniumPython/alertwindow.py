from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

nameoption = "professional"
driver.find_element_by_css_selector("#name").send_keys(nameoption)

# if there is ok button in pop up window
driver.find_element_by_id("alertbtn").click()
alartdriver = driver.switch_to.alert
alartmsg = alartdriver.text
print(alartmsg)
assert nameoption in alartmsg
alartdriver.accept()

# if there is confirm or cancel in pop up window
driver.find_element_by_id("confirmbtn").click()
confirmdriver = driver.switch_to.alert
confirmmsg = confirmdriver.text
print(confirmmsg)
num = 1
# if 1 then confirm else cancel
if num != 1:
    confirmdriver.accept()
else:
    confirmdriver.dismiss()
