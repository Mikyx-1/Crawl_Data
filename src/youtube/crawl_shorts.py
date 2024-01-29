import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import subprocess

def find_vid_urls1(string_doc, keyword='href="/shorts/'):
    start_idx = 0
    end_idx = len(string_doc) - len(keyword)
    window_length = len(keyword)
    results = []
    for i in range(start_idx, end_idx):
        if string_doc[i:i+window_length] == keyword:
#             results.append(i)
            results.append(string_doc[i:].split(" ")[0].split("/")[-1][:-1])
    results = list(set(results))
    return results

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@schannelvn/shorts") # Put the main page here
time.sleep(5)
last_scroll_position = 0
new_scroll_position = 1
i = 0
while new_scroll_position != last_scroll_position:
    i+=1
    driver.execute_script(f"window.scrollTo(1, {str(5000*i)})")
    last_scroll_position = new_scroll_position
    new_scroll_position = driver.execute_script("return window.pageYOffset;")
    time.sleep(5)
    print(f"New scroll position: {new_scroll_position}, Last scroll position: {last_scroll_position}")

soup = BeautifulSoup(driver.page_source, "html.parser")

string_doc = str(soup)
urls = find_vid_urls1(string_doc, keyword='href="/shorts/')
for url in urls:
    download_video("https://www.youtube.com/shorts/" + url)
