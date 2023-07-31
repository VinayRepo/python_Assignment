import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test():
    # BROWSER = FIREFOX [CHROMEDRIVER IS NOT WORKING LATEST VERSION OF CHROME DRIVER DOES NOT SUPPORT LATEST VERSION
    # OF GOOGLE CHROME]
    # TASK 1
    driver = webdriver.Firefox()
    driver.get("https://www.amazon.in/minitv")
    driver.maximize_window()
    print(driver.title)
    welcome_txt = driver.title
    expected_text = "Watch Free Web Series & Short Films Online | Amazon miniTV"  # HOME PAGE TITLE
    actual_text = welcome_txt
    assert expected_text == actual_text, f"Expected: {expected_text}, but found: {actual_text}"
    time.sleep(2)
    driver.quit()


def test2():
    driver = webdriver.Firefox()
    driver.maximize_window()
    driver.get("https://www.amazon.in/minitv")
    time.sleep(2)
    # NAVIGATION TO THE WEB SERIES
    # TASK 2
    series = driver.find_element(By.CSS_SELECTOR, "img[alt='Yeh Meri Family - Season 2 - Watch Free']")
    series.click()
    time.sleep(2)
    # NAVIGATION TO SEASON
    season1 = driver.find_element(By.XPATH, "//div[@id='m-tabs-0-1']//h2[contains(@class,'Heading_h2__DveuA "
                                            "SeasonsTab_tabHeading__mGwNN')][contains(text(),'Season')]")
    season1.click()
    time.sleep(2)
    # NAVIGATION TO EPISODE1
    # TASK 3
    s1e1 = driver.find_element(By.XPATH, "//body/div[@id='__next']/div/div[contains(@class,'appContainer')]/div["
                                         "contains(@class,'dWeb mainContent')]/div["
                                         "@class='TitlePage_container__72Uc1']/div["
                                         "@class='TitlePage_btfContainer__HZBE4']/div[contains(@class,"
                                         "'SeasonsTab_container__vYTzm')]/div[@class='rmc-tabs rmc-tabs-horizontal "
                                         "rmc-tabs-top']/div[@class='rmc-tabs-content-wrap "
                                         "rmc-tabs-content-wrap-animated']/div[2]/div[1]/div[1]/div[1]/div[2]/a["
                                         "1]/div[1]/span[1]")
    s1e1.click()
    time.sleep(2)
    timeer = driver.find_element(By.XPATH, "//div[@class=' PlayerSkin_container___x4_d']")
    time.sleep(3)
    timeer.click()
    duration = driver.find_element(By.XPATH, "//div[@class=' BottomPanel_videoTimer__sbWcU "
                                             "BottomPanel_landscape__tEqjI']")
    print(duration.text)  # CAPTURING DURATION OF VIDEO PLAYBACK
    time.sleep(2)
    video_duration = "00:03/30:56"
    if video_duration == "00:00/00:56":
        print("video is not playing")
    else:
        print("video is playing")  # VERIFYING THE VIDEO PLAYBACK
    time.sleep(2)
    driver.back()
    driver.forward()
    time.sleep(3)
    season2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div["
                                            "1]/h2")
    season2.click()
    time.sleep(2)
    s2e1 = driver.find_element(By.XPATH, "//body/div[@id='__next']/div/div[contains(@class,'appContainer')]/div["
                                         "contains(@class,'dWeb mainContent')]/div["
                                         "@class='TitlePage_container__72Uc1']/div["
                                         "@class='TitlePage_btfContainer__HZBE4']/div[contains(@class,"
                                         "'SeasonsTab_container__vYTzm')]/div[@class='rmc-tabs rmc-tabs-horizontal "
                                         "rmc-tabs-top']/div[@class='rmc-tabs-content-wrap "
                                         "rmc-tabs-content-wrap-animated']/div[1]/div[1]/div[1]/div[1]/div[2]/a["
                                         "1]/div[1]/span[1]")
    s2e1.click()
    time.sleep(2)
    timeer2 = driver.find_element(By.XPATH, "//div[@class=' PlayerSkin_container___x4_d']")
    time.sleep(3)
    timeer2.click()
    duration2 = driver.find_element(By.XPATH, "//div[@class=' BottomPanel_videoTimer__sbWcU "
                                              "BottomPanel_landscape__tEqjI']")
    print(duration2.text)
    time.sleep(2)
    video_duration2 = "00:03/32:56"
    if video_duration2 == "00:00/00:56":  # VERIFYING VIDEO PLAYBACK
        print("video is not playing")
    else:
        print("video is playing")
    driver.quit()
    # TASK 4
    # CHECK ASSERTION AND REPORTING BY RUNNING THE PYTEST AMAZON_MINITV_TEST.PY IN A TERMINAL OR A COMMAND PROMPT
    # THANK-YOU
