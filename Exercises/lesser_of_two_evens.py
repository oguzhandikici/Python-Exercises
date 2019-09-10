## iki sayidan en az biri ciftse ikisinden buyugune, ikisi de tekse kucuk olana return.
def lesser_of_two_evens(a,b):
	aOdd = a%2
	bOdd = b%2
	oddCount=aOdd+bOdd
	if oddCount in [1,2]:
		return max(a,b)
	else:
		return min(a,b)
##Check
result=lesser_of_two_evens(int(input('1. Sayiyi girin:  ')), int(input('2. Sayiyi girin:  ')))
print(result)
