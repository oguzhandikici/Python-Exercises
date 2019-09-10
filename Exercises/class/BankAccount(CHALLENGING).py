class Account:

	def __init__(self,owner='Oguzhan',balance=4000):
		self.owner=owner
		self.balance=balance
		print('\nAccount Created!\nOwner: {}\nBalance: {}'.format(self.owner,self.balance))

	def deposit(self,amount):
		self.balance=self.balance+amount
		print('\nDeposited the amount {}!\nCurrent Balance: {}'.format(amount,self.balance))

	def withdraw(self,amount):
		if self.balance>=amount:
			self.balance=self.balance-amount
			print('Withdrawn the amount {}!\nCurrent Balance: {}'.format(amount,self.balance))
		else:
			print('Amount Exceeds Balance!')
##Check
myacc=Account(input('Hesap ismi girin:  '),int(input('Hesapta olacak tutari girin:  ')))
while True:
	choice=int(input('\nNe yapmak istersiniz? (1: Para yatirma, 2: Para cekme):  '))
	if choice==1:
		myacc.deposit(float(input('\nYatirilacak miktari girin:  ')))
		another=int(input('\nBaska islem yapmak ister misiniz? (1:Evet, 2:Hayir):  '))
		if another==1:
			continue
		elif another==2:
			break
	elif choice==2:
		myacc.withdraw(float(input('\nCekilecek miktari girin:  ')))
		another=int(input('\nBaska islem yapmak ister misiniz? (1:Evet, 2:Hayir):  '))
		if another==1:
			continue
		elif another==2:
			break
	else:
		print('\nHatali giris. Tekrar deneyin.')
input('Cikmak icin [ENTER] basin.')