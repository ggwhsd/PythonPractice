# -*- coding: UTF-8 -*-
#背包问题
def knap_rec(weight, wlist,n):
	if weight == 0:
		print("step 1 "+str(weight)," ", wlist[n-1]," ["+str(n)+"]")
		return True
	if weight < 0 or (weight>0 and n<1):
		print("step 2 "+str(weight)," ", wlist[n-1]," ["+str(n)+"]")
		return False
	if knap_rec(weight - wlist[n-1], wlist, n-1):
		print("step 3 "+str(weight)," ", wlist[n-1]," ["+str(n)+"]")
		print("Item "+str(n)+":",wlist[n-1])
		return True
	if knap_rec(weight, wlist, n-1):
		print("step 4 "+str(weight)," ", wlist[n-1]," ["+str(n)+"]")
		return True
	else:
		return False

wlist=[3,1,5,6,9,2]
knap_rec(8,wlist,6)