#! /usr/bin/env python3
from selenium import webdriver
import time, bs4, requests

base ='https://mp.weixin.qq.com'
name = '凤凰新闻'
accountList = ['央视新闻', '新浪新闻','凤凰新闻']
searchURL = "http://weixin.sogou.com/weixin?type=1&s_from=input&query={}".format(name)

res = requests.get(searchURL)
res.raise_for_status()
soup = bs4.BeautifulSoup(res.text, "lxml")
# get the 1st URL
account = soup.select('a[uigs="account_name_0"]')
time.sleep(1)
accountURL = account[0]['href']

# go to detail page 
res = requests.get(accountURL)
res.raise_for_status()


print(accountURL)
browser = webdriver.PhantomJS("/Users/chasechoi/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
browser.get(accountURL)


time.sleep(3)
# html = browser.execute_script("return document.documentElement.outerHTML")
html = browser.page_source
accountSoup = bs4.BeautifulSoup(html, "lxml")

time.sleep(2)
contents = accountSoup.find_all(hrefs=True)

partitialLink = contents[0]['hrefs']
firstLink = base + partitialLink
print(firstLink)

# visit the content
res = requests.get(firstLink)
res.raise_for_status()
detailPage = bs4.BeautifulSoup(res.text, "lxml")
print(detailPage.title.text)
myfile = open('/Users/chasechoi/Downloads/newsContent.html', 'wb')
myfile.write(res.content)
myfile.close()





