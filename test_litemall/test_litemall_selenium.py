import time

import allure
from selenium import webdriver

from selenium.webdriver.chrome.service import Service


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# 替换为实际的ChromeDriver路径
path_to_chromedriver = 'C:/Program Files/Google/Chrome/Application/chromedriver.exe'
service = Service(executable_path=path_to_chromedriver)

class TestLitemall:
    # 前置操作
    def setup_class(self):
        self.driver = webdriver.Chrome(service=service)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    # 后置操作
    def teardown_class(self):
        self.driver.quit()

    def getscreen(self):
        timestamp = int(time.time())
        image_path = f"./image/image_{timestamp}.png"
        # 截图
        self.driver.save_screenshot(image_path)
        # 放在报告中
        allure.attach.file(image_path, name='picture',
                           attachment_type=allure.attachment_type.PNG)

    # 登录
    def test_search(self):
        self.driver.get("https://litemall.hogwarts.ceshiren.com/")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("hogwarts")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("test12345")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='品牌制造商']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[placeholder='请输入品牌商名称']").send_keys("花生")
        self.driver.find_element(By.XPATH, "//*[text()='查找']").click()
        time.sleep(2)
        self.getscreen()
        res = self.driver.find_elements(By.XPATH, "//*[text()='花生']")

        assert res != []
        self.getscreen()



    def test_edit(self):
        self.driver.get("https://litemall.hogwarts.ceshiren.com/")
        self.driver.find_element(By.NAME, "username").clear()
        self.driver.find_element(By.NAME, "username").send_keys("hogwarts")
        self.driver.find_element(By.NAME, "password").clear()
        self.driver.find_element(By.NAME, "password").send_keys("test12345")
        self.driver.find_element(By.CSS_SELECTOR, ".el-button--primary").click()
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='品牌制造商']").click()
        # 显示等待
        ele = WebDriverWait(self.driver,10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, "//*[text()='1062728']/../..//*[text()='编辑']")))
        ele.click()
        # self.driver.find_element(By.XPATH, "//*[text()='1062728']/../..//*[text()='编辑']").click()
        # 新增按钮
        # self.driver.find_element(By.CSS_SELECTOR, ".el-icon-edit").click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-form-item__content>.el-input--mini>.el-input__inner').clear()
        self.driver.find_element(By.CSS_SELECTOR,'.el-form-item__content>.el-input--mini>.el-input__inner').send_keys("霍格沃兹")
        self.driver.find_element(By.XPATH, "//*[text()='确定']").click()
        # 获取成功msg,断言
        res = self.driver.find_elements(By.XPATH,"//*[text()='霍格沃兹']")
        # 数据清理
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[text()='1062728']/../..//*[text()='编辑']").click()
        self.driver.find_element(By.CSS_SELECTOR, '.el-form-item__content>.el-input--mini>.el-input__inner').clear()
        self.driver.find_element(By.CSS_SELECTOR, '.el-form-item__content>.el-input--mini>.el-input__inner').send_keys(
            "OPPO")
        self.driver.find_element(By.XPATH, "//*[text()='确定']").click()

        assert  res != []

        time.sleep(5)

