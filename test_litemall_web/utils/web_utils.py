from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_litemall_web.utils.log_utils import logger


def click_exception(by, element, max_attempts=5):
    def _inner(driver):
        # 实际点击次数
        ac_attempts = 0
        while ac_attempts < max_attempts:
            # 进行点击操作
            ac_attempts += 1
            # 每次循环，实际点击次数加1
            try:
                # 点击过程中出错，直接执行except，并继续循环
                # 未出错，则直接return，循环结束
                driver.find_element(by, element).click()
                return True
            except Exception:
                logger.debug("点击时出现了一次错误")
        # 当实际点击次数超过最大次数，结束循环，抛出异常
        raise Exception("超出最大点击次数")

    # return _inner() 错误写法，应返回对象而非方法
    return _inner


