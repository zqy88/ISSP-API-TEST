import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login_individual(url, username, pwd):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    driver.get(url)
    # 用户名
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)
    # 密码
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(pwd)
    # 复选框
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "el-checkbox__input")))
    driver.find_element("class name", "el-checkbox__input").click()
    # 登录按钮
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'el-button input-item-btn')]")))
    driver.find_element(By.XPATH, "//button[contains(@class,'el-button input-item-btn')]").click()
    sleep(10)
    token = driver.execute_script('return localStorage.getItem("USER_TOKEN");')
    Userid = driver.execute_script('return localStorage.getItem("USERID_RSA");')
    driver.close()
    return token, Userid


def login_enterprise(url, username, pwd):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    driver.get(url)
    # 选择企业账号登录
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,
                                        "//*[@id='__layout']/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]")))
    driver.find_element(By.XPATH, "//*[@id='__layout']/div/div/div[2]/div/div[2]/div/div[1]/div/div[2]/div[2]").click()
    # 用户名
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text']")))
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)
    # 密码
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(pwd)
    # 复选框
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "el-checkbox__input")))
    driver.find_element("class name", "el-checkbox__input").click()
    # 登录按钮
    WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'el-button input-item-btn')]")))
    driver.find_element(By.XPATH, "//button[contains(@class,'el-button input-item-btn')]").click()
    sleep(10)
    token = driver.execute_script('return localStorage.getItem("USER_TOKEN");')
    Userid = driver.execute_script('return localStorage.getItem("USERID_RSA");')
    driver.close()
    return token, Userid


def login_admin(url, username, pwd):
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options)
    driver.maximize_window()
    # 登陆
    driver.get(url)
    # 用户名
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH,  "//input[@type='text']")))
    driver.find_element(By.XPATH, "//input[@type='text']").send_keys(username)
    # 密码
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//input[@type='password']")))
    driver.find_element(By.XPATH, "//input[@type='password']").send_keys(pwd)
    # 点击按钮
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(@class,'submit-button')]")))
    driver.find_element(By.XPATH, "//button[contains(@class,'submit-button')]").click()
    sleep(10)
    token = driver.execute_script('return localStorage.getItem("ACCESS_TOKEN");')
    driver.close()
    return token[1:len(token)-1]













