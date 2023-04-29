from selenium import webdriver
from time import sleep


class SpeedTest:
    def __init__(self):
        self.SPEEDTEST_URL = "https://www.speedtest.net/"
        self.chrome_driver_path = "V:\Development\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=self.chrome_driver_path)
        self.download_speed = 0
        self.upload_speed = 0

    def get_up_and_down_speeds(self):
        self.driver.get(url=self.SPEEDTEST_URL)
        self.driver.maximize_window()

        go_button = self.driver.find_element_by_class_name("start-text")
        go_button.click()
        sleep(42)
        self.download_speed = self.driver.find_element_by_class_name("download-speed").text
        self.upload_speed = self.driver.find_element_by_class_name("upload-speed").text
        self.driver.quit()
