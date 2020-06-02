from selenium import webdriver
import time

option = webdriver.ChromeOptions()
option.add_argument('--headless')
option.add_argument('--disable-gpu')
driver = webdriver.Chrome("D://softwareinstall//python//python36//chromedriver.exe", chrome_options=option)
driver.get("https://www.baidu.com")
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()
time.sleep(3)
# cookies = driver.get_cookies()
# print(cookies)
# cookies = {i['name'] : i['value'] for i in cookies}
# print(cookies)
print(driver.page_source)
driver.save_screenshot("./baidu.png")
driver.quit()