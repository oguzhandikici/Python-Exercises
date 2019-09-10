##Kullanicidan alinan sayi listesi icinde yine kullanicidan alinan 3 sayi sirali bir sekilde varsa True, yoksa False return.
def spy_game(num,order):
	level=1
	result=False
	numList=[int(input('{}. sayiyi girin:  '.format(num+1))) for num in range(num)]
	print(numList)
	for i in range(num):
		if numList[i]==order[0] and level==1:
			level=2
			continue
		elif numList[i]==order[1] and level==2:
			level=3
			continue
		elif numList[i]==order[2] and level==3:
			result=True
			return result
	return result
##Check
result=spy_game(int(input('Kac sayi gireceksiniz:  ')),[int(input('Sirasi dikkate alinacak {}. sayiyi girin:  '.format(x+1))) for x in range(3)])
print(result)