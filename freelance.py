from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import random


with open("proxy_list.txt", "r") as f: 
    proxies = f.read().split("\n") 



PROXY_LIST = []

for i, proxy in enumerate(proxies):
    host, port = proxy.split(':')
    PROXY_LIST.append({'host': host, 'port': port})


# Loop through the list of proxies
for proxy in PROXY_LIST:
    # Set up the proxy configuration
    proxy_options = {
        'proxy' : {
            'httpProxy': f'http://{proxy["host"]}:{proxy["port"]}',
            'sslProxy': f'https://{proxy["host"]}:{proxy["port"]}',
            'noProxy': ''
        }
    }
  
    PROXY_HOST = "1.224.3.122"	
    PROXY_PORT = "3889"
    # Set up the Chrome options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--ignore-ssl-errors')
    chrome_options.add_argument('--ignore-local-proxy')
    chrome_options.add_argument('--proxy-server=http://{PROXY_HOST}:{PROXY_PORT}')
    # Select a random proxy server from the list
    # proxy = random.choice(proxies)
    
    # Set up the Chrome browser with the proxy server
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--proxy-server=http://' + proxy)
    driver = webdriver.Chrome(r"C:\Users\skander\Downloads\chromedriver-win64\chromedriver.exe", options=chrome_options)
    
    
    
    time.sleep(3)
    driver.get('https://strawpoll.com/w4nWrAW2lyA') 
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