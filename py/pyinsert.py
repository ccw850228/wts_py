# -*- coding: utf-8 -*
from dbconn import DBConn
import time 

sTime = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())
print sTime
try:
	dbuse = DBConn()
		
	dbuse.dbConn()
		
	sql = "INSERT INTO hello (name, phone, time) VALUES ('wei', '0909', '%s')" % (sTime)  
	dbuse.runInsert(sql)
	
	dbuse.dbClose()
	
except:
	print "error"