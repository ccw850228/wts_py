# -*- coding: utf-8 -*-
import os
import codecs
import sys
import re
from dbconn import DBConn
import time

matrix = [[None for i in range(7)] for i in range(100000)]

x=0
y=0
z=1

for root, dirs, files in os.walk(u"台灣電力公司_計畫性工作停電資料/wkotgnews/"):
    #print root
    for f in files:
        #print (os.path.join(root, f))
		#rt = str(os.path.join(root, f))
		print (f)
		fo = codecs.open(u'台灣電力公司_計畫性工作停電資料/wkotgnews/%s'%(f), 'r', 'utf-8', 'ignore')
		#fo = codecs.open(u'台灣電力公司_計畫性工作停電資料/wkotgnews/109.txt', 'r', 'utf-8', 'ignore')
		next(fo)
		str = fo.read()
		enc= (str.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
		#print enc
		sp = re.split('#|\r\n',enc)
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
			
		print u"文件名: ", fo.name
		fo.close()
		
#for nu in range(10):
#	print matrix[nu][0]+'\000'+matrix[nu][1]


#if matrix[124][0]=='\r\n':
#	print 'true'
#else:	
#	print matrix[124][0]

try:
	dbuse = DBConn()
	
	dbuse.dbConn()
	
	sql = "TRUNCATE TABLE s_elect "
	dbuse.runTrun(sql)
	
	dbuse.dbClose()

except:
	print "erreor"



try:
	for x in range(10000):
		print x
		print matrix[x][0]+"\000"+matrix[x][1]+"\000"+matrix[x][2]+"\000"+matrix[x][3]+"\000"+matrix[x][4]+"\000"+matrix[x][5]+"\000"+matrix[x][6]	
		#print matrix[124][0]
	
		dbuse = DBConn()
		
		dbuse.dbConn()
		
		sql = "INSERT INTO s_elect (name, code, worktype, firststop, secondstop,stoprange, phone ) VALUES \
		('%s', '%s','%s','%s','%s','%s','%s')" % (matrix[x][0],matrix[x][1],matrix[x][2],matrix[x][3],matrix[x][4],matrix[x][5],matrix[x][6])  
		dbuse.runInsert(sql)
	
		dbuse.dbClose()
	
#time.sleep(0.01)
		
except Exception as e:
	print(e.message)

	

