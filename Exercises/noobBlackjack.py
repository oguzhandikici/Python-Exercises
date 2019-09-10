import random
def blackjack(a,b,c):
	sumNums=a+b+c
	if sumNums>21 and 11 in (a,b,c):
		sumNums=sumNums-10
		if sumNums==21:
			return 'BLACKJACK!'
		elif sumNums<21:
			return '{}!'.format(sumNums)
		else:
			return 'BUST'
	elif sumNums==21:
		return 'BLACKJACK!'
	else:
		return '{}!'.format(sumNums)
##Check
trial=blackjack(random.randint(1,11),random.randint(1,11),random.randint(1,11))
print(trial)