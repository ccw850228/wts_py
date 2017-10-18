#!/usr/bin/python
# -*- coding: utf-8 -*-
import csv
import sys
from linux_dbconn import DBConn

matrix = [[None for i in range(7)] for i in range(200)]
reload(sys)
sys.setdefaultencoding('utf-8')
x=0
#f = open('/s_water.csv', 'r')
num=0
id=1
#print matrix
#1
for count in range(1,8): 
	f = open('s_water.csv', 'r')
	num=0
	for row in csv.DictReader(f, [u"1",u"2",u"3",u"4",u"5",u"6",u"7"]):
		str = row['%s'%count]
		if str==None:
			str='nothing'
			#enc= (str.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
			matrix[num][count-1]=str
			#print matrix[num][count-1]
			#print num
			num+=1

		else:
			#enc= (str.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
			matrix[num][count-1]=str
			#print matrix[num][count-1]
			#print num
			num+=1
	f.close()

try:
	dbuse = DBConn()
	
	dbuse.dbConn()
	
	sql = "TRUNCATE TABLE s_water "
	dbuse.runTrun(sql)
	
	dbuse.dbClose()

except:
	print "erreor"



try:
	for x in range(200):
		print x
		print matrix[x][0]+"\000"+matrix[x][1]+"\000"+matrix[x][2]+"\000"+matrix[x][3]+"\000"+matrix[x][4]+"\000"+matrix[x][5]+"\000"+matrix[x][6]	
		#print matrix[124][0]
	
		dbuse = DBConn()
		
		dbuse.dbConn()
		
		sql = "INSERT INTO s_water (reason, s_range, s_period, re, phone, c_period, c_area ) VALUES \
		('%s', '%s','%s','%s','%s','%s','%s')" % (matrix[x][0],matrix[x][1],matrix[x][2],matrix[x][3],matrix[x][4],matrix[x][5],matrix[x][6])  
		dbuse.runInsert(sql)
	
		dbuse.dbClose()
	
#time.sleep(0.01)
		
except Exception as e:
	print(e.message)

	