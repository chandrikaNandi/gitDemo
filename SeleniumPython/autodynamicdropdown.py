
from selenium import webdriver

import time  # this class is required for the method sleep()

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/dropdownsPractise/")
# it is a example of Automatic dynamic dropdown
# first we have to send some substring, like for country dropdown send substring 'Ind'
driver.find_element_by_id("autosuggest").send_keys("Ind")
time.sleep(2)  # time class has to be imported for the mathod sleep(), here sleep() method is required because after
# sending keyword browser may take 1 or 2 sec to show the dropdown list...in the meantime selenium might search the list
# and the script might fail

# dropdown open with the matching substring(developer's job),  then we will collect all element matching substring
# using Css traverse locator (parent child tag) in a variable
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))

# to select the desired element in dropdown we run a for loop, with the if condition checking every element
# when desired element match then use click() method and then break the loop
for country in countries:
    print(country.text)
    if country.text == "India":
        country.click()
        break

# here we can not use driver.find_element_by_id("autosuggest").text as in run time it will not show any text,
# so it returns blank. for that we have to use get_attribute('value') method to capture the value
print(driver.find_element_by_id("autosuggest").get_attribute('value'))
# checking if the desired element is selected or not after click() method
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"