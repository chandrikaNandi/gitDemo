# selenium locators are very essential for automation testing
# using a hrml form to check and edit value

from selenium import webdriver

from selenium.webdriver.support.select import Select  # this is to import Select class for dropdown menu
#for any browser code is same only change is the name of exe file of that browser. rest syntax are same
driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")

# driver.find_element_by_id("autocomplete").send_keys("TEST")  # syntax of id and name locators are same

driver.find_element_by_css_selector("input[id='autocomplete']").send_keys("test1")   # syntax of css locators
# in the browser console we must write  $("input[id='autocomplete']") to check the syntax and then enter
# for the selenium css locator

#driver.find_element_by_xpath("//*input[text()='Radio3']").click()

#driver.find_element_by_xpath("//button['@id=openwindow']").click()   # syntax of xpath locators

# in the browser console we must write  $x("//button['@id=openwindow']") to check the syntax and then enter
# for the selenium css locator

# [id*='autocomplete']  -is the regular expression for CSS, if it is unique then tagname here input/label optional
# //*[contains(@id,'autocomplete')] -is the regular expression for XPATH, if it is unique then tagname optional
driver.find_element_by_id("checkBoxOption2").click()   # syntax of checkbox locators
driver.find_element_by_name("checkBoxOption1").click()

msg = driver.find_element_by_class_name("blinkingText").text
print(msg)  # to grab the text in the web element

# for dropdown menu selenium Select class has to be import

dropdownselect = Select(driver.find_element_by_id("dropdown-class-example"))
dropdownselect.select_by_visible_text("Option2")
dropdownselect.select_by_index(0)
dropdownselect.select_by_value("option3")

# we can also use assert keyword to check the entire program is running ok or not.
# assert returns true or false, if true it runs successfully, if false it shows error

#assert "FREE" in msg  # if we want to check FREE substring present in msg variable
assert "Limited offer - FREE Core Java & QA Resume course" == msg  # if the whole string is = to msg variable


#---------------------------------------------------------------------------------------




