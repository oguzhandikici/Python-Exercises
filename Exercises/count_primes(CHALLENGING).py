def primeCheck(primenum):
	'''
	result=True ise primenum=Prime,
	result=False ise primenum=non-Prime.
	'''
	result=True
	dividerList=list(range(2,primenum))
	for i in range(len(dividerList)):
		if primenum%dividerList[i]==0:
			result=False
			return result
			break
	return result

def count_primes(num):
	'''
	num sayisi dahil, num sayisina kadar tum asal sayilari bulur.
	'''
	global sayi #num global denilince error veriyor.
	sayi=num
	numList=list(range(2,num+1))
	primeList=[]
	for i in range(len(numList)):
		if primeCheck(numList[i]):
			primeList.append(numList[i])
	return primeList
##Check
result=count_primes(int(input('Sayi girin:  ')))
print('{} sayisina kadar tum asal sayilar:'.format(sayi))
print(result)