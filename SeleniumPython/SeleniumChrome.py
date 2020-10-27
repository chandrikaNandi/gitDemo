from selenium import webdriver

# driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")  # driver is an object of class webdriver

# driver = webdriver.Firefox(executable_path="C:\\geckodriver.exe")

driver = webdriver.Opera(executable_path="C:\\operadriver.exe")

driver.get("https://www.facebook.com")  # it opens a pop up window with mentioned URL

driver.maximize_window()

print(driver.title)  # show the title of the website, checking it in the console

print(driver.current_url)  # very useful, normally shows the mentioned URL but when hacked the give the different URL

driver.get("https://www.google.co.in")  # facebook.com is changed to google.co.in in yhe same window

driver.minimize_window()

driver.back()   # back to facebook.com
driver.refresh()   # if any code there in second url which effect the first one, so it must refresh to get updated data

driver.close()  #  it closes the current window, in programing if we have to open more than one windows and then close
# driver.quit()  # it closes all the windows open that time
