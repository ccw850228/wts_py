# -*- coding: utf-8 -*
from linux_dbconn import DBConn




try:
	dbuse = DBConn()
	
	dbuse.dbConn()
	
	sql = "TRUNCATE TABLE s_water "
	dbuse.runTrun(sql)
	
	dbuse.dbClose()

except Exception as e:
	print(e.message)