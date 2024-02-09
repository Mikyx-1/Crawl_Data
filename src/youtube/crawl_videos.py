import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import subprocess

def find_vid_urls(string_doc, keyword='href="/watch?v='):
    '''
    Args: string_doc: stringified html file
          keyword: the element locating the vid url
    
          output: All the video urls 
    '''
    start_idx = 0
    end_idx = len(string_doc) - len(keyword)
    window_length = len(keyword)
    results = []
    for i in range(start_idx, end_idx):
        if string_doc[i:i+window_length] == keyword:
            link_vid = "https://www.youtube.com/"  + string_doc[i:i+2000].split(" ")[0].split("/")[1][:-1]
            results.append(link_vid)
    
    return list(set(results))

driver = webdriver.Chrome()
driver.get("https://www.youtube.com/@schannelvn/videos") # Put the main page here
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

video_urls = find_vid_urls(string_doc)
