# import threading 
# import queue
import requests

# q= queue.Queue() 
# valid_proxies = []

# with open("proxy_list.txt", "r") as f: 
#     proxies = f.read().split("\n") 
#     for p in proxies: 
#         q.put(p)

# def check_proxies():
#     global q
#     while not q.empty():
#         proxy = q.get()
#         try:
#             res = requests.get("http://ipinfo.io/json", 
#                                proxies = {"http": proxy,
#                                           "https:" :proxy})
#         except:
#             continue
#         if res.status_code == 200:
#             print (proxy)

# for _ in range(10):
#     threading.Thread(target=check_proxies).start()


from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import time

# change 'ip:port' with your proxy's ip and port
proxy_ip_port = '162.223.94.163:80'

proxy = Proxy()
proxy.proxy_type = ProxyType.MANUAL
proxy.http_proxy = proxy_ip_port
proxy.ssl_proxy = proxy_ip_port

capabilities = webdriver.DesiredCapabilities.CHROME
proxy.add_to_capabilities(capabilities)

# replace 'your_absolute_path' with your chrome binary absolute path
driver = webdriver.Chrome(r"C:\Users\skander\Downloads\chromedriver-win64\chromedriver.exe", desired_capabilities=capabilities)

driver.get('http://www.google.com')

time.sleep(8)

driver.quit()