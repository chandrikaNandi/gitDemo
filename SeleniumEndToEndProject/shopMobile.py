from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://rahulshettyacademy.com/angularpractice/")

driver.find_element_by_xpath("//a[contains(text(),'Shop')]").click()

select_mobiles = driver.find_elements_by_xpath("//div[@class='card h-100']")

# //div[@class='card h-100']/div/h4/a this is the full path, as locator is already in //div[@class='card h-100 so we
# only have to write the rest
for mobile in select_mobiles:
    #add items into cart
    if mobile.find_element_by_xpath("div/h4/a").text == 'Blackberry':
        mobile.find_element_by_xpath("div/button").click()
# as //div[@class='card h-100'] path is already contains by mobile object we can rest path
# in line 17 instead of giving div[@class='card-footer']/button path we can give index of div like div[2]/button
# or we can simply put div/button button is the child tag only div[2] parent tag so div/button is unique also

# line 23 contains the full traverse back path of the add button
#add_mobile = select_mobile.find_element_by_xpath("parent::h4/parent::div/parent::div/div[@class='card-footer']/button")

driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
time.sleep(3)
assert driver.find_element_by_css_selector("h4[class='media-heading']").text == "Blackberry"

products_list = driver.find_elements_by_xpath("//tbody/tr")
final_item = len(products_list)-2

for list_item in products_list[0: final_item]:
    print(list_item.find_element_by_xpath("td[1]/div/div/h4").text)
    print(list_item.find_element_by_xpath("td[4]").text)

total_amount = driver.find_element_by_xpath("//td[5]/h3").text
if total_amount != '':
    print("check out")
    driver.find_element_by_css_selector("button[class='btn btn-success']").click()


driver.find_element_by_css_selector("#country").send_keys("Ind")
#time.sleep(10)
# here we have to put explicit wait
wait = WebDriverWait(driver, 7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element_by_link_text("India").click()

driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()

driver.find_element_by_css_selector("input[value='Purchase']").click()

print(driver.find_element_by_class_name("alert-success").text)
# you can also check by assert method

# how to take screen shot of web pages
driver.get_screenshot_as_file("screenshot_test.png")
















