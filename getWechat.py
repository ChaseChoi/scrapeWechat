#! /usr/bin/env python3
from selenium import webdriver
import time
import bs4
import requests, re

base ='https://mp.weixin.qq.com'
name = "广东共青团"
searchURL = "http://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=y&_sug_type_=&w=01019900&sut=1139&sst0=1508495544059&lkt=0%2C0%2C0".format(name)
res = requests.get(searchURL)
res.raise_for_status()
pattern = re.compile(r':"/s\?[=*;&\d\w]+"')
soup = bs4.BeautifulSoup(res.text, "lxml")
# get the corresponding URL
account = soup.select('a[uigs="account_name_0"]')
accountURL = account[0]['href']

res = requests.get(accountURL)
res.raise_for_status()
accountSoup = bs4.BeautifulSoup(res.text, "lxml")
time.sleep(3)
scripts = accountSoup.find_all("script")
scriptText = scripts[-2].text
print(scriptText)
extractURL = pattern.search(scriptText)
time.sleep(3)
print(extractURL.group())
sliced = extractURL.group()
part = sliced[2:-1]
print(part)

