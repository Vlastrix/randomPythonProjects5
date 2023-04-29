from selenium import webdriver
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

INSTAGRAM_LOG_URL = "https://www.instagram.com/"
USERNAME = "YOUR USERNAME"
PASSWORD = "YOUR PASS"
ACCOUNT_URL = "https://www.instagram.com/instagram/"

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Logging in

driver.get(url=INSTAGRAM_LOG_URL)
driver.maximize_window()
sleep(4)

username_input = driver.find_element_by_name("username")
username_input.send_keys(USERNAME)

password_input = driver.find_element_by_name("password")
password_input.send_keys(PASSWORD)
sleep(1)
log_in_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
log_in_button.click()

# Going to the account

sleep(6)
driver.get(ACCOUNT_URL)

followers_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
followers_button.click()
sleep(4)

scr1 = driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')

# Scrolling first
for i in range(10):
    driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scr1)
    sleep(2)

# Then following everyone
# DON'T FORGET TO USE CSS SELECTORS LIKE I DID IN THE PAST

follow_buttons = driver.find_elements_by_css_selector("li button")
for button in follow_buttons:
    try:
        button.click()
        sleep(1)
    except ElementClickInterceptedException:
        cancel_button = driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
        cancel_button.click()
