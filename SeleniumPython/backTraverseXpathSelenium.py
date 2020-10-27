import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.implicitly_wait(5)

driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector(".search-keyword").send_keys('be')
time.sleep(4)

vegContainer = driver.find_elements_by_xpath("//div[@class= 'product']")  # for verification

print(len(vegContainer))

addKart = driver.find_elements_by_css_selector("div [class='product-action'] button")

# this the back traverse path of Xpath  //div[@class='product-action']/button/parent::div/parent::div/h4
# back traverse syntax {with no space}is from the particular cursor point here //div[@class='product-action']/button add
# /parent::parenttag(if goto grand parent the again add)/parent::parenttag(and then required element)/h4
# CSS can not go back from child to parent, it gives only one way parent to child
# we are using back traverse to optimize our coding and working maximum in one loop instead of using multiple loops
for vegs in addKart:
    print(vegs.find_element_by_xpath('parent::div/parent::div/h4').text)
    # VERY CAREFUL HERE. AS POINTER IS ON 'vegs'
    # WE HAVE TO WRITE vegs.find_element_by_xpath INSTEAD  driver.find_element_by_xpath AND PATH SHOULD BE
    # parent::div/parent::div/h4 AS 'vegs' = //div[@class='product-action']/button ALREADY

    vegs.click()

driver.find_element_by_css_selector("a.cart-icon").click()


