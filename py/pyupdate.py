# -*- coding: utf-8 -*
from dbconn import DBConn

try:
	dbuse = DBConn()
	
	dbuse.dbConn()
	
	sql = "UPDATE hello SET name='imChange' WHERE id='1'"
	dbuse.runUpdate(sql)
	
	dbuse.dbClose()

except:
	print "erreor"