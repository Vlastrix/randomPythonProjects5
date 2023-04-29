from selenium import webdriver
from time import sleep

SPEEDTEST_URL = "https://www.speedtest.net/"
TWITTER_URL = "https://twitter.com/login?lang=en"
MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASS"

chrome_driver_path = "V:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# GETTING SPEED CONNECTION

driver.get(url=SPEEDTEST_URL)
driver.maximize_window()

go_button = driver.find_element_by_class_name("start-text")
go_button.click()
sleep(42)

download_speed = driver.find_element_by_class_name("download-speed").text

upload_speed = driver.find_element_by_class_name("upload-speed").text

# FINISHING SPEED CONNECTION

# LOGGING TO TWITTER START

driver.get(TWITTER_URL)
sleep(6)
email_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/'
                                           'div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
email_input.send_keys(MY_EMAIL)
sleep(1)
next_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
                                           '/div[2]/div[2]/div[2]/div/div')
next_button.click()
sleep(2)
password_input = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
                                              '/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
password_input.send_keys(MY_PASSWORD)
sleep(1)
log_in_button = driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]'
                                             '/div[2]/div[2]/div/div')

log_in_button.click()

# LOGGING TWITTER END

# PUBLISHING TWEET

sleep(2)

tweet_text = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div'
                                          '[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div'
                                          '/div/label/div[1]/div/div/div/div/div/div/div/div/div')

tweet_text.send_keys(f"Hey Internet Provider, why is my internet speed {download_speed}down/{upload_speed}up when I pay"
                     f" for 100down/30up?")

tweet_button = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div'
                                            '/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
tweet_button.click()

sleep(16)
driver.quit()

# PUBLISHING TWEET END
