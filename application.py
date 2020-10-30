from selenium import webdriver
import os.path

url_admin = 'http://10.0.36.121:83'
username1 = 'admin'
password1 = '10Uyjvjd.'


class Application:

    def __init__(self):
        self.driver = webdriver.Chrome(os.path.abspath(os.curdir) + '\driver\chromedriver.exe')
        self.driver.implicitly_wait(60)
        self.driver.maximize_window()

    def login(self, username, password):
        driver = self.driver
        driver.get(url_admin + "/admin/login/")
        driver.find_element_by_id('id_username').send_keys(username)
        driver.find_element_by_id("id_password").send_keys(password)
        driver.find_element_by_xpath("//input[@type='submit']").click()

    def destroy(self):
        self.driver.quit()
