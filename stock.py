import time
from bs4 import BeautifulSoup
url = r'http://vip.stock.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid=%s&type=mgjzc' % 600844 # 每股净资产数据
try:
    html = urllib2.urlopen(url).read()
except:
    
    print 'need sleep!'
    time.sleep(300) #网站为了防止频繁抓取，会自动关闭访问，所以需要休眠几分钟，然后重新开始抓。
    html = urllib2.urlopen(url).read()
         
soup = BeautifulSoup(html)
tablesoup = soup.find('table', attrs = {'id':'Table1'})
rows = tablesoup.find_all('tr') #找出所有行
d = {}
for row in rows[1:]:
    data = row.find_all('td')
    d.setdefault(data[0].get_text(strip = True), data[1].get_text(strip = True)) # {'riqi':'mgjzc'}
 
for k, v in d.items(): # 清除字典中的空集
    if v == '':
        d[k] = 0.0
