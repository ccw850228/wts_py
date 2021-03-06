# -*- coding: utf-8 -*-
import urllib2
from bs4 import BeautifulSoup
from dbconn import DBConn
import time 

html_doc = """
<HTML lang="zh-TW">
<HEAD><TITLE>行政院人事行政總處全球資訊網-天然災害停止上班及上課情形查詢</TITLE>
<META http-equiv=Content-Type content="text/html; charset=UTF-8">
<META content="MSHTML 6.00.2800.1400" name=GENERATOR></HEAD>
<BODY bgColor=#dcdbc2>
<TABLE width="100%" border=0>
  <TBODY>
  <TR>
    <TD width="100%" colSpan=3 id="T_PA">
      <p align=center><EM><STRONG><FONT color=#408080 
      size=6>行政院人事行政總處</FONT></STRONG><FONT color=#408080 
      size=4>　<STRONG>全球資訊網</STRONG></FONT></EM></p></TD></TR>
  <TR>
    <TD width="100%" colSpan=3 headers="T_PA Descritpion">
      <h2 align=center><STRONG><FONT color=#008080 
      size=4>106年7月31日 天然災害停止上班及上課情形</FONT></STRONG><FONT size=3></h2>
      <p align=right><a href="ndse.html">ENGLISH VERSION</a></P>	
      </TD></TR>
  <TR>
    <TD width="33%"></TD>
    <TD width="21%"></TD>
    <TD width="46%" headers="T_PA date">
      <P align=right ><FONT color=#000000 size=2>更新時間： 2017/07/31 18:31:30</FONT></P></TD>
  <TR>
    <TD width="33%"></TD>
    <TD width="21%"></TD>
    <TD width="46%" headers="T_PA history">
      <P align=right ><FONT color=#000000 size=2><a href="https://www.dgpa.gov.tw/informationlist?uid=374">歷次天然災害停止上班上課訊息</a></FONT></P></TD>
  <TR>
    <TD width="33%" headers="T_PA gov"><FONT size=2>資料來源：各縣市政府</FONT></TD>
    <TD width="21%"></TD>
    <TD width="46%" align="right">
</FONT>
<a href="contact/Tel.htm"><FONT size=2>
民眾洽詢天然災害停止上班及上課各地方政府連絡一覽表
</FONT></a>      <P></P></TD></TR></TBODY></TABLE>
<TABLE cellSpacing=1 width="100%" bgColor=#cdfad9 border=1>
  <TBODY style="font-size: 15px;">
      <TR>
          <Th width="13%" bgColor=#008080 id="city_Name">
              <P align=center>
                  <STRONG>
                      <FONT color=#ffffff
                            size=3>縣市名稱</FONT>
                  </STRONG>
              </P>
          </Th>
          <Th width="70%" bgColor=#008080 id="StopWorkSchool_Info">
              <P align="left">
                  <STRONG>
                      <FONT color=#ffffff
                            size=3>是否停止上班上課情形</FONT>
                  </STRONG>
              </P>
          </Th>
      </TR>
<TR><TD vAlign=center align=middle width='13%'><FONT size=2>基隆市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>臺北市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>新北市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>桃園市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>新竹市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>新竹縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>苗栗縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>臺中市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT><br><FONT color=#FF0000 size=2>臺中市和平區平等國民小學、臺中市和平區立幼兒園平等班、臺中市和平區梨山國民中小學: 今天停止上班、停止上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>彰化縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>雲林縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>南投縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>嘉義市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>嘉義縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT><br><FONT color=#FF0000 size=2>嘉義縣義竹鄉南興國民小學: 今天停止上班、停止上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>臺南市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#FF0000 size=2>今天停止上班、停止上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>高雄市</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#FF0000 size=2>今天停止上班、停止上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>屏東縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#FF0000 size=2>今天停止上班、停止上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>宜蘭縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>花蓮縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>臺東縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT><br><FONT color=#FF0000 size=2>延平鄉紅葉村、延平鄉鸞山村上野地區: 今天停止上班、停止上課。  </FONT><br><FONT color=#800080 size=2>臺東縣長濱鄉樟原國民小學: 今天照常上班、停止上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>澎湖縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>連江縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR><TR><TD vAlign=center align=middle width='13%'><FONT size=2>金門縣</FONT></TD><TD vAlign=center align=left width='70%'><FONT color=#000080 size=2>今天照常上班、照常上課。  </FONT></TD></TR>

  <td width="100%" colspan=3 style='width:100.0%;background:#F2DCF3;padding:
  .75pt .75pt .75pt .75pt'  headers="T_PA Note">
  <!-- <p class=MsoNormal><span style='font-size:10.0pt;color:#000040'>備註：機關、學校中英文名稱係由各通報機關提供。</span> </p>-->

  <p class=MsoNormal><span style='font-size:10.0pt;color:#000040'>備註：</span> </p>
  <ol start=1 type=1>
   <li class=MsoNormal style='color:#333399;mso-margin-top-alt:auto;mso-margin-bottom-alt:
       auto;mso-list:l0 level1 lfo3;tab-stops:list 36.0pt'><span
       style='font-size:10.0pt'>若欲進入本總處網站首頁版面，請按
<SPAN lang=EN-US><A href="https://www.dgpa.gov.tw"><SPAN style="COLOR: red">人事行政總處全球資訊網</SPAN></A>

。 </SPAN></SPAN><SPAN 
        lang=EN-US><O:P></O:P></SPAN>        
   <li class=MsoNormal style='color:#333399;mso-margin-top-alt:auto;mso-margin-bottom-alt:
       auto;mso-list:l0 level1 lfo3;tab-stops:list 36.0pt'><span
       style='font-size:10.0pt'>機關、學校中英文名稱係由各通報機關提供。</span> <span lang=EN-US><o:p></o:p></span></li> 

</OL></TD></TR></TBODY></TABLE><P align=left><STRONG><FONT color=#FF0000       size=3>偽造、變造本總處網頁發布不實訊息者，可能涉嫌觸犯刑法第211條：
「偽造、變造公文書，足以生損害於公眾或他人者，處一年以上七年以下有期徒刑。」
之偽造公文書罪或可能涉嫌觸犯刑法第360條：
「無故以電腦程式或其他電磁方式干擾他人電腦或其相關設備，致生損害於公眾或他人者，
處三年以下有期徒刑、拘役或科或併科十萬元以下罰金。」之干擾他人電腦罪，請勿以身試法，以免觸犯刑責。<br>
依天然災害停止上班及上課作業辦法第10條規定<br>
通報權責機關決定停止上班及上課時，應於下列時間前對外發布：<br>
（一）全日或上午半日停止上班及上課時：應於前一日晚間7時至10時前
         發布，並通知傳播媒體於晚間11時前播報之。但前一日未發布當
         日停止上班及上課，於當日0時後，風雨增強，經參酌交通部中央
         氣象局提供各地區最新風力級數、陣風級數及雨量預測列表等氣象資料，
         已達第4條第1款、第2款之基準時，通報權責機關應於當日上午4時30分前發布，
         並通知傳播媒體，於上午5時前播報之。<br>
（二）下午半日或晚間停止上班及上課時：應於當日上午10時30分前發
         布，並通知傳播媒體，於上午11時前播報之。
（三）除上開時間外，各通報權責機關得視實際情形，隨時發布之。
  </FONT></STRONG><FONT size=3> 
    </FONT></P></BODY></HTML>


	"""


soup = BeautifulSoup(html_doc, "lxml")
area = soup.find_all('td', width='13%')
status = soup.find_all('td',width='70%')
exc = soup.find_all('font',color='#FF0000',size='2')
#建立字典
dic = {u'基隆市':'1',u'臺北市':'2',u'新北市':'3',u'桃園市':'4',u'新竹市':'5',\
u'新竹縣':'6',u'苗栗縣':'7',u'臺中市':'8',u'彰化縣':'9',u'雲林縣':'10',\
u'南投縣':'11',u'嘉義市':'12',u'嘉義縣':'13',u'臺南市':'14',u'高雄市':'15',\
u'屏東縣':'16',u'宜蘭縣':'17',u'花蓮縣':'18',u'臺東縣':'19',u'澎湖縣':'20',u'連江縣':'21',u'金門縣':'22'}
#print dic['基隆市']
#建立串列
matrix = [[None for i in range(2)] for i in range(50)]
num=0
count=0
uc=0
my_list=[]

sTime = time.strftime("%Y-%m-%d  %H:%M:%S", time.localtime())

for y in area:
	num=num+1
	print str(num)+y.string
	ycon = unicode(y.string) #轉unicode
	matrix[num][0] = ycon #放入串列
	if dic.has_key(ycon):
		print 'true'
	else:
		print 'err'

for x in status:
	count=count+1
	print(str(count)+x.font.string)
	xcon = unicode(x.font.string)
	matrix[count][1] = xcon
	
for z in exc:
	print z.string
	

for u in area :
	uc = uc+1
	print str(uc)+u.string
	ucon = unicode(u.string)
	if dic.has_key(ucon):
		print 'true'
		try:
			dbuse = DBConn()
	
			dbuse.dbConn()
	
			sql = "UPDATE swork SET country='%s',status='%s',uTime='%s' WHERE id='%s'" % (matrix[uc][0], matrix[uc][1],sTime,dic[ucon])  
			dbuse.runUpdate(sql)
	
			dbuse.dbClose()

		except:
			print "erreor"
	else:
		print 'err'
	
#print matrix[16][0]
#print matrix[16][1]			

	
	

