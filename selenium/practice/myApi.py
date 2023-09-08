from selenium.webdriver.common.by import By
import cv2
from scapy import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import base64
import datetime
time.mktime(datetime.datetime.now().date().timetuple())


class PicProcess:
    def base64_to_img_file(self, base64_str, file_path):
        str1 = re.sub(r'%0A', "\\n", base64_str)
        str2 = re.sub(r'data:image/png;base64,', '', str1)
        imgdata = base64.b64decode(str2)
        file = open(file_path, 'wb')
        file.write(imgdata)
        file.close()
        time.sleep(1)

    def get_distance_block_left_to_canvas_left(self, canvas_img_path, block_img_path):
        # 以灰度模式加载背景图
        canvas_gray = cv2.imread(canvas_img_path, 0)
        # 以灰度模式加载滑块图片
        block_gray = cv2.imread(block_img_path, 0)
        # 匹配小图在大图中的位置-匹配模式
        res = cv2.matchTemplate(canvas_gray, block_gray, cv2.TM_CCORR_NORMED)
        # 匹配背景图中缺口最左边到背景图最左边边缘的结果
        value = cv2.minMaxLoc(res)
        # print(value)
        # 大图中缺口最左边到大图最左边的距离
        x = value[2][0]
        print(f"图库计算出的初始滑动距离为:{x}")
        return x

    def get_actual_slide_dis(self, match_dis):
        if match_dis < 120:
            error = int(match_dis * 10 / 120)
        else:
            error = int(10 + (match_dis - 120) * 6 / 160)
        actual_dis = match_dis + error
        return actual_dis

    def get_tracks(self, distance):
        # 移动轨迹
        tracks = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0
        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 5
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度
            v = v0 + a * t
            # 移动距离
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            tracks.append(round(move))
        return tracks


class MySe:
    def __init__(self, driver):
        self.driver = driver

    def target(self, xpath):
        return WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        # return self.driver.find_element(By.XPATH, xpath)

    def target_click(self, xpath):
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.find_element(By.XPATH, xpath).click()

    def target_send_keys(self, xpath, mystr):
        WebDriverWait(self.driver, 2).until(
            EC.presence_of_element_located((By.XPATH, xpath))
        )
        self.driver.find_element(By.XPATH, xpath).send_keys(mystr)
