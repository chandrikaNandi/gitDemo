from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# path locator should be common one as here type='checkbox' then selenium locator would find all the elements of togather
# here we have to be careful as the return elements are more than one we use elements_by instead of element_by
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
# if condition can be put inside for loop if there is certain condition
for checkitem in checkboxes:
    print(checkitem.get_attribute('value'))  # we can check the values of the element, it is required if we use condition
    checkitem.click()  # here it will click all the checkbox in loop
    assert checkitem.is_selected()  # checked check box is selected or not, if false give error


# for radiobutton
# in radio button only one option can be selected, so we don't need loop or iteration
radioButtons = driver.find_elements_by_name("radioButton")
radioButtons[2].click()  # as elements stored in a list here radioButtons, it starts with 0 index


