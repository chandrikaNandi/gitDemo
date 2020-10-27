import time
from selenium import webdriver

#  the three classes below we have to import for selenium explicit wait method
from selenium.webdriver.support.wait import WebDriverWait
from  selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

vegInCart = []
cartProduct = []
sumPrice = 0

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")

driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector(".search-keyword").send_keys('be')
time.sleep(4)

vegContainer = driver.find_elements_by_xpath("//div[@class= 'product']")  # for verification

print(len(vegContainer))

addKart = driver.find_elements_by_css_selector("div[class='product-action'] button")

for vegs in addKart:
    # taking all the vegetables in cart in variable vegInCart
    vegInCart.append(vegs.find_element_by_xpath('parent::div/parent::div/h4').text)
    vegs.click()

driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()


# Explicit wait syntax, it is explicitly for the command which need wait to work, it is not global
wait = WebDriverWait(driver, 10)   # WebDriverWait(who will wait, how much time) these two parameters
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, 'input.promoCode')))
# it tells wait for this particular element (pointing its location) and wait until what is expected from the element
# double parenthesis (()) for By method syntax

productNo = driver.find_elements_by_xpath("//p[@class='product-name']")
print(len(productNo))

for cartCheck in productNo:
    cartProduct.append(cartCheck.text)

print(cartProduct)
print((vegInCart))

# check if product in cart and product in billing page are same or not
assert cartProduct == vegInCart

totalAmount = driver.find_element_by_xpath("//span[@class='discountAmt']").text
print(totalAmount)
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("[class='promoBtn']").click()
# ones wait object is created it can be used in multiple times
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[@class='promoInfo']")))

discAmount = driver.find_element_by_xpath("//span[@class='discountAmt']").text
print(discAmount)
assert float(discAmount) < int(totalAmount)  # verifying discount rate

print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)

# checking the sum of price is matching with total value
vegPriceCount = driver.find_elements_by_xpath("//tbody/tr/td[5]")

for vegPrice in vegPriceCount:
    sumPrice = sumPrice + int(vegPrice.text)
print(sumPrice)
assert sumPrice == int(totalAmount)


