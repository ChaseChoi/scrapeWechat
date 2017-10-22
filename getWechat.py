#! /usr/bin/env python3
from selenium import webdriver
from datetime import datetime
import bs4, requests
import os, time, sys

def getAccountURL(searchURL):
	res = requests.get(searchURL)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "lxml")
	# get the 1st URL
	account = soup.select('a[uigs="account_name_0"]')
	time.sleep(10)
	return account[0]['href']

def getArticleURL(accountURL):
	# go to detail page 
	browser = webdriver.PhantomJS("/Users/chasechoi/Downloads/phantomjs-2.1.1-macosx/bin/phantomjs")
	browser.get(accountURL)

	html = browser.page_source
	accountSoup = bs4.BeautifulSoup(html, "lxml")
	time.sleep(2)
	contents = accountSoup.find_all(hrefs=True)
	try:
		partitialLink = contents[0]['hrefs']
		firstLink = base + partitialLink
	except IndexError:
		firstLink = None 
		print('CAPTCHA!')
	return firstLink

def folderCreation():
	path = os.path.join(os.getcwd(), datetime.now().strftime('%Y-%m-%d_%H-%M-%S'))
	try:
		os.makedirs(path)
	except OSError as e:
		if e.errno != errno.EEXIST:
			raise
		print("folder not exist!")
	return path
def writeToFile(path, title):
	myfile = open("{}/{}.html".format(path, title), 'wb')
	myfile.write(res.content)
	myfile.close()

base ='https://mp.weixin.qq.com'
accountList = ['央视新闻', '新浪新闻','凤凰新闻','羊城晚报', '罗辑思维', '小sa神', '亚马逊Kindle']
query = 'http://weixin.sogou.com/weixin?type=1&s_from=input&query='

path = folderCreation()
for index, account in enumerate(accountList):

	searchURL = query + account
	accountURL = getAccountURL(searchURL)
	articleURL = getArticleURL(accountURL)
	if articleURL != None:
		print("#{}({}/{}): {}".format(account, index+1, len(accountList), accountURL))
		# visit the content
		res = requests.get(articleURL)
		res.raise_for_status()
		detailPage = bs4.BeautifulSoup(res.text, "lxml")
		title = detailPage.title.text
		print("标题: {}\n链接: {}\n".format(title, articleURL))
		writeToFile(path, title)
	else:
		sys.exit()


print('{} files successfully written to {}'.format(len(accountList), path))




