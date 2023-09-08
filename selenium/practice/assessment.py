from myService import *
import pandas as pd


url = "https://www.cz-iis.com/login"
username = 15168216773
pwd = "chongai111"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options)
driver.maximize_window()
driver.get(url)
login(driver, username, pwd)

se = MySe(driver)
se.target_click("//*[@id='__layout']/div/div[1]/div/div[2]/div[1]/ul/li[8]/span")


def fun1():
    for i in range(12):
        temp = "E:\\pythonWorkSpace\\api_test_1" \
               "\\selenium\\practice\\assess"+str(i+1)+".xls"
        print(temp)
        se.target_click("//*[@id='__layout']/"
                        "div/div[2]/div[2]/div/div/div[1]/div[2]/div[2]")
        fun2(temp)


def fun2(temp):
    df = pd.read_excel(temp, names=None)
    df_li = df.values.tolist()
    print(df_li)
    for i in range(19):
        for j in range(8):
            x = df_li[i][j]
            y = str(x)
            if y[0] != "n":
                se.target_click("//*[@id='__layout']/div/div[2]/div[2]/div/form/div["+str(i+1) +
                                    "]/div[2]/div[" + str(j+1) + "]/div/div/label[" + y[0] + "]/span[1]/span")
                if j == 7:
                    se.target_click("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/button[3]/span")
            else:
                if i != 18:
                    se.target_click("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/button[3]/span")
                break
    se.target_click("//*[@id='__layout']/div/div[2]/div[2]/div/div[1]/button[4]/span")
    se.target_click("/html/body/div[2]/div/div[3]/button/span")


fun1()
sleep(600)
