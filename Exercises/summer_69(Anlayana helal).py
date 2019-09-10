##Girilen sayı listesinden 6-9(arası ve dahil) dışındaki sayılar toplanır.
def summer_69(num):
	summ=0
	dummysum=0
	dummy=False
	numList=[int(input('{}. sayiyi girin:  '.format(num+1))) for num in range(num)]
	for i in range(num):
		if numList[i]==6 or dummy==True:
			dummy=True
			dummysum+=numList[i]
			if numList[i]==9:
				dummy=False
				dummysum=0
		else:
			summ+=numList[i]
	summ+=dummysum
	return summ
##Check
result=summer_69(int(input('Kac sayi gireceksiniz:  ')))
print(result)