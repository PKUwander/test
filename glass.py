
#!/usr/bin/env python 
#-*- coding:utf-8 -*-


#百个眼镜，摆成一个圈，全部正面向上，第一个人将每个翻动一次，一共翻了100次；第二个人从no.2开始隔一个翻一次，也翻100次；第3个人从no.3开始隔两个翻一次，翻100次，问100个人之后，多少眼镜正面向上

import numpy as np
l=[]
n=100
a=np.zeros(n)
for  i  in range(1,n+1):

	for j in range(i,(n+1)*i,i):
		
		while(j>n):
			if(j<=n):
				if(a[j-1]==0):
					a[j-1]=1
				else: 
					a[j-1]=0
			else:
				j=j-n
		if(a[j-1]==0):
			a[j-1]=1
		else: 
			a[j-1]=0
			

for x in range(n):
	if(a[x]==0):
		l.append(x+1)
print l
	