# -*- coding: utf-8 -*-
#my_list=[['taipei','stop'],['kao','unstop']]
import codecs
import sys
import re

#print(text.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))

 
sum=0
#print my_list[1][0]+my_list[1][1]
matrix = [[None for i in range(2)] for i in range(30)]
#台灣電力公司_計畫性工作停電資料/wkotgnews/101.txt
fo = codecs.open(u'台灣電力公司_計畫性工作停電資料/wkotgnews/101.txt', 'r', 'utf-8', 'ignore')
#fo.write( "www.runoob.com!\nVery good site!\n");
str = fo.read(10000);
enc= (str.encode(sys.stdin.encoding, "replace").decode(sys.stdin.encoding))
print enc
print type(enc)
sp = re.split('#',enc)
for x in sp:
	print x
	print sum
	sum+=1

#str =fo.read(3000);
#print u"讀 : ", str 
print u"文件名: ", fo.name

# 关闭打开的文件
fo.close()
