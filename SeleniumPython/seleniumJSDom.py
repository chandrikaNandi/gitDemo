# JS DOM can access any web element in web page just like how selenium does
# selenium has a method to execute javascript in it, the use of it is very rare

from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_name("name").send_keys("Chandrika")

print(driver.find_element_by_name("name").text)  # it can not be fetched the text from the element as the text is given
# through selenium script, if browser loads the text then it can be fetched by this method

print(driver.find_element_by_name("name").get_attribute("value"))  # get_attribute() will fetch the value.
# it is nothing but a javascript in build in selenium

# instead of using selenium code it also give permission to javascript by execute_script() method to execute script
print(driver.execute_script("return document.getElementsByName('name')[0].value;"))

# javascript (made in browser console) document.getElementsByName('name')[0].value have to write return before it
# so that the value goes to the selenium object

clickButton = driver.find_element_by_css_selector("a[href='/angularpractice/shop']")  # instead of doing click() method
# let's try it in javascript as sometime due to overlapping of buttons selenium might not operate that time javascript
# do it inside the html code
driver.execute_script("arguments[0].click();", clickButton)

# selenium has NO METHOD to scroll web page, javascript is helping here too
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")



