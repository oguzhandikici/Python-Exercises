##Cumledeki kucuk ve buyuk karakterleri sayar.
def up_lows(str):
	strList=str.split()
	spacelessStr=''.join(strList)
	loweredSentence=spacelessStr.lower()
	upperedSentence=spacelessStr.upper()
	lowerCount=[1 for x in range(len(loweredSentence)) if spacelessStr[x]==loweredSentence[x]]
	upperCount=[1 for x in range(len(upperedSentence)) if spacelessStr[x]==upperedSentence[x]]
	print('No. of Upper case characters: {}'.format(sum(upperCount)))
	print('No. of Lower case characters: {}'.format(sum(lowerCount)))
##Check
up_lows(input('Cumle girin:  '))
