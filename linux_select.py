# -*- coding: utf-8 -*-
import os
import codecs
import sys
import re
from linux_dbconn import DBConn
import time
import geocoder


matrix = [['0' for i in range(9)] for i in range(100000)]
reload(sys)
sys.setdefaultencoding('utf-8')

x=0
y=0
z=1

for root, dirs, files in os.walk(u"wkotgnews/"):
    #print root
    for f in files:
        #print (os.path.join(root, f))
		#rt = str(os.path.join(root, f))
		print (f)
		#fo = codecs.open(u'wkotgnews/%s'%(f), 'r', 'utf-8', 'ignore')
		fo = codecs.open(u'wkotgnews/101.txt', 'r', 'utf-8', 'ignore')
		#fo = codecs.open(u'台灣電力公司_計畫性工作停電資料/wkotgnews/109.txt', 'r', 'utf-8', 'ignore')
		next(fo)
		str = fo.read()
		#enc= (str.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
		#print enc
		#sp = re.split('#|\r\n',enc)
		sp = re.split('#|\r\n',str)
		for value in sp:
			if value != '\r\n':
				if value != '':
					matrix[x][y] = value
					y+=1
					if y==7:
						y=0
						x+=1
				
				elif value==u'' and y==5:
					value.replace(u'',u'nothing')
					matrix[x][y] = value
					y+=1
			
		#print u"文件名: ", fo.name
		fo.close()
		
try:
	for num in range(10):
		g = geocoder.google('%s'%matrix[num][5])
		print matrix[num][5]
		print g.latlng
		matrix[num][7] = g.lat
		matrix[num][8] = g.lng
		time.sleep(0.1)
		
except Exception as e:
	print(e.message)

try:
	dbuse = DBConn()
	
	dbuse.dbConn()
	
	sql = "TRUNCATE TABLE s_elect "
	dbuse.runTrun(sql)
	
	dbuse.dbClose()
	print "true"

except:
	print "erreor"



try:
	for x in range(10):
		#print x
		#print matrix[x][0]+"\000"+matrix[x][1]+"\000"+matrix[x][2]+"\000"+matrix[x][3]+"\000"+matrix[x][4]+"\000"+matrix[x][5]+"\000"+matrix[x][6]	
		#print matrix[124][0]
	
		dbuse = DBConn()
		
		dbuse.dbConn()
		
		sql = "INSERT INTO s_elect (name, code, worktype, firststop, secondstop,stoprange, phone, lat, lng ) VALUES \
		('%s', '%s','%s','%s','%s','%s','%s','%s','%s')" % (matrix[x][0],matrix[x][1],matrix[x][2],matrix[x][3],matrix[x][4],matrix[x][5],matrix[x][6],matrix[x][7],matrix[x][8])  
		dbuse.runInsert(sql)
	
		dbuse.dbClose()
	
#time.sleep(0.01)
		
except Exception as e:
	print(e.message)

	

