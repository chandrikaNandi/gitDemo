import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe")
driver.implicitly_wait(5)  # this is an explicit wait, it is global for all web driver in the page
#  implicitly_wait(5) means it tell the web driver to wait till 5 sec, if the process is done before that then it is
#  intelligent enough to pass the pointer to next command

driver.get("https://www.rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element_by_css_selector(".search-keyword").send_keys('be')
time.sleep(4)

vegContainer = driver.find_elements_by_xpath("//div[@class= 'product']")  # for verification

print(len(vegContainer))

addKart = driver.find_elements_by_css_selector("div[class='product-action'] button")

for vegs in addKart:
    vegs.click()

driver.find_element_by_css_selector("a.cart-icon").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_css_selector("input.promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector("[class='promoBtn']").click()
print(driver.find_element_by_xpath("//span[@class='promoInfo']").text)


