from utils.support import get_webdriver


def before_all(context):
    """

    :type context: object
    """
    context.browser = get_webdriver()
    context.browser.maximize_window()
    context.browser.delete_all_cookies()


def after_all(context):
    context.browser.quit()
