from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests
import shutil

# create a new Chrome browser instance
browser = webdriver.Chrome(r"C:\Users\skander\Downloads\chromedriver-win64\chromedriver.exe")

# navigate to Instagram
browser.get('https://www.instagram.com')

# log in to Instagram
username = browser.find_element_by_name('username')
password = browser.find_element_by_name('password')
username.send_keys('your_username')
password.send_keys('your_password')
password.send_keys(Keys.RETURN)

# wait for the home page to load
time.sleep(5)

# navigate to the Explore page
browser.get('https://www.instagram.com/explore/')

# wait for the Explore page to load
time.sleep(5)

# find the first trending post and click on it
trending_post = browser.find_element_by_xpath('//div[@class="v1Nh3 kIKUG  _bz0w"]/a')
trending_post.click()

# wait for the post to load
time.sleep(5)

# get the video URL and download the video
video_url = browser.find_element_by_xpath('//video').get_attribute('src')
response = requests.get(video_url, stream=True)
with open('video.mp4', 'wb') as f:
    shutil.copyfileobj(response.raw, f)

# navigate to the Reels page
browser.get('https://www.instagram.com/reels/')

# wait for the Reels page to load
time.sleep(5)

# click on the Create Reel button
create_reel_button = browser.find_element_by_xpath('//button[@class="wpO6b "]')
create_reel_button.click()

# wait for the Create Reel page to load
time.sleep(5)

# upload the video
upload_button = browser.find_element_by_xpath('//input[@type="file"]')
upload_button.send_keys(os.getcwd() + '/video.mp4')

# wait for the video to upload
time.sleep(5)

# add a caption and post the Reel
caption = browser.find_element_by_xpath('//textarea[@aria-label="Write a caption…"]')
caption.send_keys('Check out this trending video!')
post_button = browser.find_element_by_xpath('//button[@class="sqdOP yWX7d    y3zKF     "]')
post_button.click()

# wait for the Reel to post
time.sleep(5)

# close the browser
browser.quit()