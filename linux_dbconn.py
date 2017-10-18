# -*- coding: utf-8 -*-
import MySQLdb

class DBConn:
	def __init__(self):
		self.user = 'root'
		self.host = 'localhost'
		self.passwd = 'whenstop153'
		self.dbname = 'wts'
	
	def dbConn(self):
		self.db = MySQLdb.connect(self.host,self.user,self.passwd,self.dbname,charset='utf8')
		self.cursor = self.db.cursor()
		
	def runQuery(self, sql):
		self.cursor.execute(sql)
		
		self.results = self.cursor.fetchall()
	
	def dbClose(self):
		self.db.close()
		
		
	# Exec SQL Insert
	def runInsert(self, sql):
		self.cursor.execute(sql)
		self.db.commit()

  # Exec SQL Update
	def runUpdate(self, sql):
		self.cursor.execute(sql)
		self.db.commit()

  # Exec SQL Delete
	def runDelete(self, sql):
		self.cursor.execute(sql)
		self.db.commit()
	
	def runTrun(self, sql):
		self.cursor.execute(sql)
		self.db.commit()
