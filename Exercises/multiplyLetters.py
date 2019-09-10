##String alip her harfini 3 kere yazar.
def paper_doll(text):
	multipliedLetters=[]
	for i in range(len(text)):
		multipliedLetters.append(text[i]*3)
	return ''.join(multipliedLetters)
##Check
result=paper_doll(input('Kelime girin:  '))
print(result)
