# -*- coding: utf-8 -*-
import os
import codecs
import sys
import re


#os.chdir(u"台灣電力公司_計畫性工作停電資料/")
print os.getcwd()

for root, dirs, files in os.walk(u"台灣電力公司_計畫性工作停電資料/wkotgnews/"):
    print root
    for f in files:
        #print (os.path.join(root, f))
		#rt = str(os.path.join(root, f))
		print (f)
		fo = codecs.open(u'台灣電力公司_計畫性工作停電資料/wkotgnews/%s'%(f), 'r', 'utf-8', 'ignore')

		str = fo.read(50000);
		enc= (str.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
		print enc
		sp = re.split('#',enc)
		#for x in sp:
		#	print x
			
		print u"文件名: ", fo.name
		fo.close()

	
		

		
