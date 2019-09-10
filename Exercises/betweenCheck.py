##Girilen sayi 100±10 ve 200±10 ise True, yoksa False
def almost_there(n):
	return n in list(range(90,111))+list(range(190,211))
##Check
result=almost_there(int(input('Bir sayi girin:  ')))
print(result)
