import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time

def find_vid_urls1(string_doc, keyword='href="/shorts/'):
    start_idx = 0
    end_idx = len(string_doc) - len(keyword)
    window_length = len(keyword)
    results = []
    for i in range(start_idx, end_idx):
        if string_doc[i:i+window_length] == keyword:
            results.append(string_doc[i:].split(" ")[0].split("/")[-1][:-1])
    results = list(set(results))
    return results
  

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@NicholasRenotte/shorts")
time.sleep(5)

scroll_number = 3
for i in range(1, scroll_number):
    driver.execute_script(f"window.scrollTo(1, {str(5000*i)})")
    time.sleep(5)
    print(i)
soup = BeautifulSoup(driver.page_source, "html.parser")

string_doc = str(soup)
urls = find_vid_urls1(string_doc)

