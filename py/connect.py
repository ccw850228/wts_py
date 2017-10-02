# -*- coding: utf-8 -*-
from dbconn import DBConn

try:
	dbuse = DBConn()
	
	dbuse.dbConn()
	
	sql = "SELECT  id, name, phone FROM hello"
	dbuse.runQuery(sql)
	
	for record in dbuse.results:
		col0 = record[0]
		col1 = record[1]
		col2 = record[2]
		
		print "%s, %s, %s" % (col0, col1,col2)
		
	dbuse.dbClose()
except:
	print 'error'
