# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request("https://www.dgpa.gov.tw/typh/daily/nds.html")
response = urllib2.urlopen(request)
html=response.read()
soup=BeautifulSoup(html,"lxml")

h2s = soup.find_all('h2')
 
for h2 in h2s:
	#print h2.string
	if h2.string != None:
		h2con = unicode(h2.string)
		if h2con == u'無停班停課訊息。':
			print 'true'
			print h2con
		else:
			print 'false'
