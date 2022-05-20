from selenium import  webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path="C:\\Users\Admin\Downloads\chromedriver.exe")
driver.get('http://automationpractice.com/index.php?controller=authentication&back=my-account')
username = "vrpops123@gmail.com"
password = "vr@gmail.com"
email_input_box = driver.find_element_by_name("email")

password_input_box = driver.find_element_by_name("passwd")

submit_btm = driver.find_element_by_name("SubmitLogin")
email_input_box.send_keys(username)
time.sleep(2)
password_input_box.send_keys(password)
time.sleep(2)
submit_btm.click()

user_prop = '//*[@id="center_column"]/div/div[1]/ul/li[4]/a'
driver.find_element_by_xpath(user_prop).click()

user_name='//*[@id="firstname"]'
input_box=driver.find_element_by_xpath(user_name)
name = "vr@gmail.com";
input_box.send_keys(name)

cp='//*[@id="old_passwd"]'
input_boxc=driver.find_element_by_xpath(cp)
name = "vr@gmail.com";
input_boxc.send_keys(name)

submit_user='//*[@id="center_column"]/div/form/fieldset/div[11]/button'
submit_user.click()

time.sleep(1000)
