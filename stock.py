import time
from bs4 import BeautifulSoup
url = r'http://vip.stock.finance.sina.com.cn/corp/view/vFD_FinanceSummaryHistory.php?stockid=%s&type=mgjzc' % 600844 # ÿ�ɾ��ʲ�����
try:
    html = urllib2.urlopen(url).read()
except:
    
    print 'need sleep!'
    time.sleep(300) #��վΪ�˷�ֹƵ��ץȡ�����Զ��رշ��ʣ�������Ҫ���߼����ӣ�Ȼ�����¿�ʼץ��
    html = urllib2.urlopen(url).read()
         
soup = BeautifulSoup(html)
tablesoup = soup.find('table', attrs = {'id':'Table1'})
rows = tablesoup.find_all('tr') #�ҳ�������
d = {}
for row in rows[1:]:
    data = row.find_all('td')
    d.setdefault(data[0].get_text(strip = True), data[1].get_text(strip = True)) # {'riqi':'mgjzc'}
 
for k, v in d.items(): # ����ֵ��еĿռ�
    if v == '':
        d[k] = 0.0
