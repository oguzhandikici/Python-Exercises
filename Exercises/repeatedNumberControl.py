##Girilen sayida yan yana olan basamaklarda ayni sayi var mi diye kontrol eder.
def has_33(nums):
	listNums=[int(num) for num in str(nums)]
	for i in range(len(listNums)):
			try:
				if listNums[i]==listNums[i+1]:
					print('Yan yana ayni olan en az 1 sayi cifti var :(')
					break
			except IndexError:
				print('Yan yana olan tum sayilar farkli :)')
##Check
has_33(nums=int(input('Sayi girin:  ')))
