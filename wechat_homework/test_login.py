import time

import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestLogin:
    def setup(self):
        self.driver = webdriver.Chrome()

    def teardown(self):
        self.driver.quit()
    #登录保存cookie
    def test_save_cookie(self):
        #1、访问企业登录页面
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx")
        #2、扫描等待
        time.sleep(6)
        #3、获取cookies
        cookies =self.driver.get_cookies()
        print(cookies)

        #4、保存cookies
        with open("../data/cookies.yaml","w") as f:
            yaml.safe_dump(data=cookies,stream=f)

    #获取cookie
    def test_get_cookie(self):
        '''
        植入cookie
        '''
        #1、访问微信企业首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        #2、获取本地cookie
        with open("../data/cookies.yaml","r") as f:
            cookies =yaml.safe_load(f)
        #可以用一行代码获取
        # cookie =yaml.safe_load(open("cookie,yaml"))
        #3、植入cookie
        for ck in cookies:
            self.driver.add_cookie(ck)
        #4、访问微信企业首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")





