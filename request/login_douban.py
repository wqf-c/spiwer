from dama import indetify_by_filepath
from selenium import webdriver
import time
from PIL import Image
import os

driver = webdriver.Chrome()
driver.get("http://webvpn.bupt.edu.cn/login?local_login=true")
driver.find_element_by_id("user_name").send_keys("2016211824")
driver.find_element_by_xpath("//div[@class='el-input password-input']/input").send_keys("024910")

#识别验证码，直接采用截屏的方式，不用考虑cookie
img = driver.find_element_by_xpath("//div[@class='captcha-div']/a")
location = img.location
left = location['x']
top = location['y']
right = left + img.size['width']
bottom = top + img.size['height']
driver.save_screenshot("full_snap.png")
image_obj = Image.open("full_snap.png")
image_obj = image_obj.crop((left, top, right, bottom))
image_obj.save("yanzma.png")
os.remove("full_snap.png")

captcha_code = indetify_by_filepath("yanzma.png")
print(captcha_code)
#os.remove("yanzma.png")
driver.find_element_by_name("v_yzm").send_keys(captcha_code)
driver.find_element_by_id("btnSure").click()
time.sleep(20)
driver.quit()





