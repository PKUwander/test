def f(w,v,i,aw):
	global numcalls
	numcalls+=1
	print 'i:',i
	print 'numcalls',numcalls
	if i==0:
		if w[i]<=aw:
			print 'a'
			return v[i]
		else:
			print 'b'
			return 0
	wtk=f(w,v,i-1,aw)
	print 'ab'
	print 'wtk:',wtk
	if w[i]>aw:
		print 'c'
		return wtk
	else:
		print 'd'
#		print 'i',i
		wik=v[i]
		print 'wik',wik
		wik_1=wik+f(w,v,i-1,aw-w[i])
		print 'wik_1:',wik_1
	
	return max(wik_1,wtk)

w=[5,3,2]
v=[9,7,8]
numcalls=0
aw=5
res=f(w,v,len(w)-1,aw)
print 'res:',res,numcalls