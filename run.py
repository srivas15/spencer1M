import requests
import urllib2
from bs4 import BeautifulSoup

url = 'https://www.youtube.com/user/officialfifaplaya/about'
html = urllib2.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

info = soup.find("div", {"class": "about-stats"})
stats = info.find("span", {"class": "about-stat"})
subs_in_html = stats.find('b')
subs = subs_in_html.getText()

print subs

