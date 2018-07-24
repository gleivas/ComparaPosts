from selenium.webdriver.common.by import By

from utils.config_manager import config_list
from utils.support import wait_for_elements

TWITTER_POSTS = (By.XPATH, '//div[@class="js-tweet-text-container"]')


def go_to_twitter(driver):
    """

    :param driver: webelement
    :return:
    """
    twitter_url = config_list['twitter_origin']
    driver.get(twitter_url)


def assert_text_is_on_twitter(driver, text):
    """

    :param driver: webelement
    :param text: str
    :return: bool
    """

    twitter_posts = wait_for_elements(driver, TWITTER_POSTS)
    for i in range(len(twitter_posts)):
        if text == twitter_posts[i].text:
            return True
