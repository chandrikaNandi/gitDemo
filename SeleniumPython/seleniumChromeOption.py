from selenium import webdriver

chrome_option = webdriver.ChromeOptions()

chrome_option.add_argument("--start-maximized")
chrome_option.add_argument("headless")
# headless means all the work of browser goes on backend, user can not see browser, can only view the executed result

chrome_option.add_argument("--ignore-certificate-errors")

# here with executable_path we have to provide the options also so that before invoking web browser webdriver read all
# the options and then pass it through the browser
driver = webdriver.Chrome(executable_path="c:\\chromedriver.exe", options=chrome_option)

driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
