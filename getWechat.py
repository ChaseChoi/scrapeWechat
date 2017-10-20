#! /usr/bin/env python3
from selenium import webdriver
import time
import bs4
import requests, re
url = 'http://weixin.sogou.com'
base ='https://mp.weixin.qq.com'
browser = webdriver.Safari()
browser.maximize_window()
browser.get(url)

searchBox = browser.find_element_by_id('query')
searchBox.clear()
searchBox.send_keys('中国共青团')
button = browser.find_element_by_xpath('//*[@id="searchForm"]/div/input[4]')
button.click()
time.sleep(2)
account = browser.find_element_by_xpath('//*[@id="sogou_vr_11002301_box_0"]/div/div[1]/a')
accountURL = account.get_attribute('href')
print(accountURL)
time.sleep(2)
res = requests.get(accountURL)
res.raise_for_status()
pattern = re.compile(r'"content_url":"/s\?[=*;&\d\w]+"')
soup = bs4.BeautifulSoup(res.text, "lxml")

# script = soup.find_all("script", text=pattern)
scripts = soup.find_all("script")
scriptText = scripts[-2].text
extractURL = pattern.search(scriptText)
print(extractURL.group())










