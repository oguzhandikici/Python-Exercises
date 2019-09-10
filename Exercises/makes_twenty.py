##iki sayidan en az biri 20 ise veya toplamlari 20 ise return True.
def makes_twenty(n1,n2):
	return n1==20 or n2==20 or n1+n2==20
##Check
result=makes_twenty(int(input('1. sayiyi girin:  ')), int(input('2. sayiyi girin:  ')))
print(result)
