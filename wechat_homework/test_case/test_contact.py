import time
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class TestAddmeber:
    def setup(self):

        #参数化
        fake = Faker("zh_CN")
        self.username = fake.name()
        self.acctid = fake.ssn()
        self.mobile = fake.phone_number()

        #实例化
        self.driver =webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


        # 1、访问微信企业首页
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        time.sleep(2)
        # 2、获取本地cookie
        with open("../data/cookies.yaml", "r") as f:
            cookies = yaml.safe_load(f)
            print(cookies)
        # 3、植入cookie
        for ck in cookies:
            self.driver.add_cookie(ck)
        # 4、访问微信企业首页
        #     self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

    def teardown(self):
        # self.driver.quit()
        pass

    def test_add_member(self):
        # 1、点击通讯录
        self.driver.find_element(By.ID,"menu_contacts").click()
        # 2、点击添加成员按钮
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.find_element(By.XPATH, '//span[text()="添加成员"]').click()
        # 3、填写成员信息
        self.driver.find_element(By.ID, "username").send_keys(self.username)
        self.driver.find_element(By.ID, "memberAdd_english_name").send_keys("dadx")
        self.driver.find_element(By.ID, "memberAdd_acctid").send_keys(self.acctid)
        self.driver.find_element(By.ID, "memberAdd_biz_mail").send_keys("hhhhogwarts")
        self.driver.find_element(By.ID, "memberAdd_phone").send_keys(self.mobile)
        self.driver.find_elements(By.CSS_SELECTOR, "a.qui_btn.ww_btn.js_btn_save")[1].click()

    def test_add_dept(self):

        #1、点击通讯录
        self.driver.find_element(By.ID, "menu_contacts").click()
        #2、点击+
        self.driver.find_element(By.XPATH,"//*[@class='member_colLeft_top_addBtn']").click()
        #3、点击添加部门
        self.driver.find_element(By.XPATH,"//a[text()='添加部门']").click()
        #4、录入信息
        self.driver.find_element(By.NAME,"//*[@name='name]").send_keys(self.username)
        self.driver.find_element(By.XPATH,'//span[@class="js_parent_party_name"]').click()
        self.driver.find_element(By.XPATH,"//div[@class='inputDlg_item']//a[text()='测试部']").click()
        self.driver.find_element(By.XPATH,'//a[text()="确定"]').click()

        js_tips = (By.XPATH, '//*[@id="js_tips"]')
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(js_tips))
        value_tips = self.driver.find_element(*js_tips).text
        assert "新建部门成功" == value_tips