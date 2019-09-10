##Bir cumleyi tersten yazar.
def master_yoda(sentence):
	splittedSentence=sentence.split()
	splittedSentence.reverse()
	reversedSentence=' '.join(splittedSentence)
	return reversedSentence
##Check
result=master_yoda(input('Cumle girin:  '))
print(result)
