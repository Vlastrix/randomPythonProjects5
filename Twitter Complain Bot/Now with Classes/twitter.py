from selenium import webdriver
from time import sleep


class TwitterBot:
    def __init__(self):
        self.TWITTER_URL = "https://twitter.com/login?lang=en"
        self.MY_EMAIL = "YOUR EMAIL"
        self.MY_PASSWORD = "YOUR PASS"
        self.chrome_driver_path = "V:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)

    def log_in_to_twitter(self):
        self.driver.maximize_window()
        self.driver.get(self.TWITTER_URL)
        sleep(6)
        email_input = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/'
            'div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        email_input.send_keys(self.MY_EMAIL)
        sleep(1)
        next_button = self.driver.find_element_by_xpath('//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                        'div[2]/div/div'
                                                        '/div[2]/div[2]/div[2]/div/div')
        next_button.click()
        sleep(3)
        password_input = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div'
            '/div[2]/div[2]/div[1]/div/div[2]/div/label/div/div[2]/div/input')
        password_input.send_keys(self.MY_PASSWORD)
        sleep(1)
        log_in_button = self.driver.find_element_by_xpath(
            '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]'
            '/div[2]/div[2]/div/div')

        log_in_button.click()

    def publish_complain_tweet(self, down_speed, up_speed):
        sleep(2)

        tweet_text = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div'
            '[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div'
            '/div/label/div[1]/div/div/div/div/div/div/div/div/div')

        tweet_text.send_keys(
            f"Hey Internet Provider, why is my internet speed {down_speed}down/{up_speed}up when I pay"
            f" for 100down/30up?")

        tweet_button = self.driver.find_element_by_xpath(
            '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div'
            '/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div')
        tweet_button.click()

        sleep(16)
        self.driver.quit()
