
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome(r"C:\Users\skander\Downloads\chromedriver-win64\chromedriver.exe")
# driver.get("https://www.google.com/")
# # search_box = driver.find_element(By.XPATH, '//*[@id="APjFqb"]')
# search_box = driver.find_element(By.ID,"APjFqb")
# search_box.send_keys('Titanic reviews imdb')
# search_box.send_keys(Keys.ENTER)

# imdb_reviews= driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/block-component/div/div[1]/div/div/div/div/div[1]/div/div/div/div/div[2]/div/div/div[1]/div/span/a/h3')
# imdb_reviews.click()


# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Wait for the reviews to load
# reviews_loaded = WebDriverWait(driver, 10).until(
#     EC.presence_of_element_located((By.CSS_SELECTOR, ".review-container"))
# )

# # Scrape the reviews

# reviews = driver.find_elements(By.CSS_SELECTOR, ".review-container .content .text")
# for review in reviews:
#     print(review.text)


# time.sleep(5)

# driver.quit()



from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random

# Define the list of proxy servers
proxies = [
    "182.46.203.240:9999", "20.46.184.196:3128", "49.77.210.243:9999", "1.10.133.124:8080",
    "183.166.21.158:9999", "116.58.224.12:8080", "182.34.27.248:9999",  "103.102.14.8:3127",
    "114.96.62.130:3000", "123.101.231.73:9999",  "112.85.160.14:9999", 
]

# Loop 100 times to vote for the first option (q1) using a random proxy server
for i in range(1):
    # Select a random proxy server from the list
    proxy = random.choice(proxies)
    
    # Set up the Chrome browser with the proxy server
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=http://' + proxy)
    driver = webdriver.Chrome(r"C:\Users\skander\Downloads\chromedriver-win64\chromedriver.exe")#, options=chrome_options)
    
    driver.get("https://croxyproxy.com")
    time.sleep(8)
    search_bar = driver.find_element(By.XPATH,'//*[@id="url"]')
    time.sleep(3)
    search_bar.send_keys('https://strawpoll.com/w4nWrAW2lyA')
    time.sleep(5)
    search_bar.send_keys(Keys.ENTER)  
    time.sleep(4) 
    time.sleep(3)
    time.sleep(2)
    test=driver.find_element(By.XPATH,'//*[@id="html"]/body/div[5]/div[2]/div[1]/div[2]/div[2]/button[1]/p')
    time.sleep(4)  
    test.click()
    time.sleep(3)
    q1 = driver.find_element(By.XPATH,'//*[@id="option-w4nWrAW2lyA-bVg8eQzDNZY"]')
    time.sleep(6)
    q1.click()
    vote = driver.find_element(By.XPATH,'//*[@id="strawpoll_box_w4nWrAW2lyA"]/div[2]/div[1]/form/div[9]/div[2]/div/div/button/div[2]/div[3]')
    time.sleep(1)
    time.sleep(3)
    vote.click()
    time.sleep(9)

# Close the browser
driver.quit()
