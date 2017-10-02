# -*- coding: utf-8 -*-
import time
import re

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

str = u"台電高雄區營業處#H19054#管線遷移工程#2017/10/14 09:30~16:00#無##1911#"
sp = re.split('#',str)
for x in sp:
	print x 
	if x==u'':
		print 'damn'