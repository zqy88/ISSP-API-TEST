import random
from time import sleep
from selenium.webdriver import ActionChains
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import os
from myApi import *

pp = PicProcess()


def login(driver, username, pwd):
    se = MySe(driver)
    se.target_send_keys("//input[@type='text']", username)
    se.target_send_keys("//input[@type='password']", pwd)
    se.target_click("//*[@id='__layout']/div/div/div[2]/div/div[2]/div/div[1]/div/div[7]/label/span/span")
    se.target_click("//button[contains(@class,'el-button input-item-btn')]")
    sleep(0.4)
    i = 1
    while True:
        loc_canvas_img = '//img[@class="slide-canvas"]'
        loc_block_img = "//img[@class='slide-block']"
        if 0 < i < 21:
            canvas_src = se.target(loc_canvas_img).get_attribute("src")
            block_src = se.target(loc_block_img).get_attribute("src")
            canvas_img_fd = os.path.join("E:/pythonWorkSpace/issp1", 'canvas.png')
            block_img_fd = os.path.join("E:/pythonWorkSpace/issp1", 'block.png')
            pp.base64_to_img_file(canvas_src, canvas_img_fd)
            pp.base64_to_img_file(block_src, block_img_fd)
        else:
            break
        match_dis = pp.get_distance_block_left_to_canvas_left(canvas_img_fd, block_img_fd)
        if match_dis != 0:
            actual_dis = pp.get_actual_slide_dis(match_dis)
            verify_slider = se.target('//div[@class="slider-button-icon"]')
            # verify_slider = driver.find_element(By.XPATH, '//div[@class="slider-button-icon"]')
            actions = ActionChains(driver)
            actions.click_and_hold(verify_slider).perform()
            pre_slide_dis = int(actual_dis * 5 / 6)
            post_slide_dis = int(actual_dis / 6)
            actions.move_to_element_with_offset(to_element=verify_slider, xoffset=pre_slide_dis,
                                                yoffset=random.randint(-5, 5)).perform()
            tracks = pp.get_tracks(post_slide_dis)
            for track in tracks:
                actions.move_by_offset(xoffset=track, yoffset=random.randint(-5, 5)).perform()
            actions.release().perform()
            try:
                se.target_click("//button[contains(@class,'el-button input-item-btn')]")
                sleep(0.2)
            except:
                # pass
                continue
            try:
                WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, "//li[1]/span[@class='act']")))
                true_text = driver.find_element(By.XPATH, "//li[1]/span[@class='act']").text
                assert true_text == "首页"
                if True:
                    token = driver.execute_script('return localStorage.getItem("USER_TOKEN");')
                    Userid = driver.execute_script('return localStorage.getItem("USERID_RSA");')
                    return token, Userid
            except:
                i += 1
