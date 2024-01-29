import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import subprocess

driver = webdriver.Chrome()
driver.get("https://www.pexels.com/vi-vn/tim-kiem/ng%C6%B0%E1%BB%9Di/") # Put link here
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")
string_doc = str(soup)


results = []
for position in positions:
    for i in range(position, position+250):
        if string_doc[i:i+4] == ".jpg" or string_doc[i:i+4]==".png":
            results.append(string_doc[position:i+4])
            break
        elif string_doc[i:i+5] == ".jpeg":
            results.append(string_doc[position:i+5])
            break
results = list(set(results))
