import re
import getopt
import sys
import requests
from bs4 import BeautifulSoup

def GetFood(school,mode):
	url = requests.get(school)
	soup = BeautifulSoup(url.text, "lxml")
	food = soup.find("tr", { "valign" : "middle" })

	pattern = '	'
	text = food.text

	match = re.search(pattern, text)
	startIndex = match.start()
	endIndex = match.end()

	result = '{}'.format(
		text[startIndex:endIndex+40]
	)
	foods = result.strip()




	pattern = '열량:'
	text = food.text

	match = re.search(pattern, text)
	startIndex = match.start()
	endIndex = match.end()

	result1 = '{}'.format(
		text[startIndex+4:endIndex+4]
	)
	cal = result1.strip()

	f = foods + " " + cal
	fin = f.split()
	food_s = foods.split()
	cal_s = cal.split()
	if mode == 0 :
		return fin

	if mode == 1:
		return food_s

	if mode == 2 :
		return cal_s


