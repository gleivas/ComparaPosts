from selenium.webdriver.common.by import By

from utils.config_manager import config_list
from utils.support import wait_for_element

FACEBOOK_POST = (By.XPATH, '//div[@class="_5pbx userContent _3576"]')


def go_to_facebook(driver):
    """

    :param driver: webelement
    :return:
    """
    facebook_url = config_list['facebook_origin']
    driver.get(facebook_url)


def get_facebook_latest_post(driver):
    """
    
    :param driver: webelement 
    :return: str
    """
    return wait_for_element(driver, FACEBOOK_POST).text
