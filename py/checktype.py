# -*- coding: utf-8 -*-
import chardet
infile=u'台灣電力公司_計畫性工作停電資料/wkotgnews/101.txt'
rawdata = open(infile, "r").read()
result = chardet.detect(rawdata)
charenc = result['encoding']
inF=open(infile,"rb")
s=unicode(inF.read(),charenc)
inF.close()