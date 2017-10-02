# -*- coding: utf-8 -*
from dbconn import DBConn




try:
	dbuse = DBConn()
	
	dbuse.dbConn()
	
	sql = "TRUNCATE TABLE s_elect "
	dbuse.runTrun(sql)
	
	dbuse.dbClose()

except:
	print "erreor"