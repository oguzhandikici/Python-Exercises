##Kelimenin 1. ve 4. harflerini buyuterek tekrar yazar.
def old_macdonald(name):
	nameLetters=list(name)
	nameLetters[0]=nameLetters[0].capitalize()
	nameLetters[3]=nameLetters[3].capitalize()
	return ''.join(nameLetters)
##Check
result=old_macdonald(input('Kelime girin:  ')
print(result)
