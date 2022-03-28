import os
import pathlib
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TwitterScrapper:
    def __init__(self):
        self.__BASE_TWITTER_URL = 'https://twitter.com/'
        """
        As i am using chrome webdriver, i have put my chromedriver file inside directory,
        please feel free to change the path of the chromedriver according to your preference
        """
        self.__CHROME_DRIVER_PATH = os.path.join(pathlib.Path().resolve(), 'chromedriver_linux64/chromedriver')
        self.__SERVICE = Service(self.__CHROME_DRIVER_PATH)
        self.__DRIVER = webdriver.Chrome(ChromeDriverManager().install())

    def get_follower_count_by_username(self, username):
        self.__DRIVER.get(self.__BASE_TWITTER_URL + username)
        follower_url = '/{}/followers'.format(username)
        max_limit = 100
        current_sleep_time = 1
        follower_element = None
        is_found = False
        follower_number = ''
        while not is_found:
            sleep(current_sleep_time)
            try:
                follower_element = self.__DRIVER.find_element(By.XPATH, '//a[@href="' + follower_url + '"]')
                is_found = True
            except Exception as E:
                print(E)
            current_sleep_time += 1
            if current_sleep_time > max_limit:
                break
        if is_found:
            follower_number = follower_element.text
        self.__DRIVER.quit()
        return is_found, follower_number


if __name__ == '__main__':
    twitter_username = 'Benzema'
    scrapper = TwitterScrapper()
    found, total_follower = scrapper.get_follower_count_by_username(twitter_username)
    if found:
        print("Total follower for user {} is {}".format(twitter_username, total_follower))
    else:
        print("Not found")
