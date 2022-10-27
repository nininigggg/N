import time

from web_test.base import Base


class test_chrome_cookie(Base):
    def test_get_cookies(self):
        self.drvier.get("https://work.weixin.qq.com/wework_admin/frame#contacts")
        time.sleep(20)
        cookie = self.driver.get_cookies()
        print(cookie)
