#!/usr/bin/python
# -*- coding: utf-8 -*-
import MySQLdb
from pandas import DataFrame
import pandas as pd
import sqlite3
import sys
from sqlalchemy import create_engine

reload(sys)
sys.setdefaultencoding('utf-8')
host = 'localhost'
port = 3306
db = 'wts'
user = 'root'
password = 'fred7777'

engine = create_engine(str(r"mysql+mysqldb://%s:" + '%s' + "@%s/%s?charset=utf8") % (user, password, host, db))

try:
    df = pd.read_csv("swater/TaiWater_Suspend.csv")
    print(df)
    df.to_sql('swater', con=engine, if_exists='replace', index=False)
except Exception as e:
    print(e.message)