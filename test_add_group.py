from selenium import webdriver
import setting as s

driver = webdriver.Chrome(s.conf_path)


def login_admin_page(username, password):
    driver.get(s.url_admin + "/admin/login/")
    driver.find_element_by_id('id_username').send_keys(username)
    driver.find_element_by_id("id_password").send_keys(password)
    driver.find_element_by_xpath("//input[@type='submit']").click()


login_admin_page(s.username, s.password)


