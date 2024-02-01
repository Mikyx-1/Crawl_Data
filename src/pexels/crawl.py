import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import subprocess

def find_vid_urls(string_doc, keyword='https://images.pexels.com/'):
    start_idx = 0
    end_idx = len(string_doc) - len(keyword)
    window_length = len(keyword)
    results = []
    for i in range(start_idx, end_idx):
        if string_doc[i:i+window_length] == keyword:
            results.append(i)
    return results

driver = webdriver.Chrome()
driver.get("https://www.pexels.com/vi-vn/tim-kiem/ng%C6%B0%E1%BB%9Di/") # Put link here
time.sleep(5)
soup = BeautifulSoup(driver.page_source, "html.parser")
string_doc = str(soup)

positions = find_vid_urls(string_doc)


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
