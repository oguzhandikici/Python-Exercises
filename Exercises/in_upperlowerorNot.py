def ran_check(upper,lower,num):
	checkList=[x for x in range(lower,upper+1)]
	return num in checkList
##Check
result=ran_check(int(input('Ust sinir girin:  ')),int(input('Alt sinir girin:  ')),int(input('Sayi girin:  ')))
print(result)