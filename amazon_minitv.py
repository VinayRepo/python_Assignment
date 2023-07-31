import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Task 1 = Task 1: Opening Amazon MiniTV, Open the Chrome browser.
# Navigate to the Amazon MiniTV website (URL: https://www.amazon.in/minitv).
driver = webdriver.Firefox()
driver.get("https://www.amazon.in/minitv")
driver.maximize_window()
print(driver.title)
time.sleep(3)

# Task 2: Finding and Selecting a Series
# On the Amazon MiniTV homepage, locate a series of your choice (e.g., &quot;The Office&quot;).
# Click on the series to open its details page.
WebSeries = driver.find_element(By.XPATH, "//img[@alt='Yeh Meri Family - Season 2 - Watch Free']")
WebSeries.click()
time.sleep(2)

# Task 3: Playing the First Episode of Each Season
# On the series details page, find the list of seasons.
# For each season, click on the first episode to start playing it.
# Wait for the video to start playing (you can add a delay of a few seconds to ensure the video starts playing).
# Verify that the video is playing (e.g., by checking the playback status).
print(driver.title)

Season1 = driver.find_element(By.XPATH, "//div[@id='m-tabs-0-1']//h2[contains(@class,'Heading_h2__DveuA "
                                        "SeasonsTab_tabHeading__mGwNN')][contains(text(),'Season')]")
Season1.click()

S1E1 = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                            "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child("
                                            "1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > "
                                            "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child("
                                            "2) > a:nth-child(1) > div:nth-child(1) > span:nth-child(2)")
S1E1.click()
time.sleep(8)
stop = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]")
stop.click()
time.sleep(2)
close = driver.find_element(By.XPATH, "//img[@alt='close']")
close.click()

time.sleep(3)

Season2 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/div[1]/h2")
Season2.click()
S2E1 = driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                            "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child("
                                            "1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > "
                                            "div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child("
                                            "2) > a:nth-child(1) > div:nth-child(1) > span:nth-child(2)")
S2E1.click()
print(driver.title)
time.sleep(8)
stop = driver.find_element(By.XPATH, "/html/body/div[2]/div/div[1]/div[2]")
stop.click()
time.sleep(2)
close = driver.find_element(By.XPATH, "//img[@alt='close']")
close.click()

