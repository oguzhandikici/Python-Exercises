#Fonksiyonlar
def inputfunc():
	'''
	Is sayisi, islem sureleri ve teslim sureleri bu fonksiyonla ic ice liste(matris gibi) seklinde alinir.
	'''
	global isler
	global ipjdj
	ipjdj = []
	isler = list(range(1,(int(input('Is sayisini girin:	'))+1)))

	for i in range(len(isler)):
		ipjdj.append([i+1])
		ipjdj[i].append(float(input('{}. isin islem suresini (pj) girin:  '.format(i+1))))
		ipjdj[i].append(float(input('{}. isin teslim suresini (dj) girin:  '.format(i+1))))

def SPTfunc():
	'''
	En kisa islem suresine gore siralama yapilir.
	'''
	global siralama
	siralama = sorted(ipjdj, key=lambda x: x[1])
	print('\nSPT Siralamasi')
	for i in range(len(isler)):
		print('{}. sirada {} numarali is yapilacak.'.format(i+1,siralama[i][0]))

def EDDfunc():
	'''
	En erken teslim suresine gore siralama yapilir.
	'''
	global siralama
	siralama = sorted(ipjdj, key=lambda x: x[2])
	print('\nEDD Siralamasi\n')
	for i in range(len(isler)):
		print('{}. sirada {} numarali is yapilacak.'.format(i+1,siralama[i][0]))

def latenessfunc():
	'''
	Islerin istenenden ne kadar erken veya gec bitirildigi hesaplanir.
	'''
	cj = []
	t = 0
	lateness = []
	tardiness = []

	for i in range(len(isler)):
		t += siralama[i][1]
		cj.append(t)
	for i in range(len(isler)):
		lateness.append(cj[i]-siralama[i][1])
	for i in range(len(isler)):
		if ( lateness[i] < 0 ):
			tardiness.append(0)
		else:
			tardiness.append(lateness[i])
			
	print('\nLATENESS\n')
	for i in range(len(isler)):
		print('{}. siradaki is icin {}'.format(i+1,lateness[i]))
	print('\nTARDINESS\n')
	for i in range(len(isler)):
		print('{}. siradaki is icin {}'.format(i+1,tardiness[i]))

def siralamafunc():
	'''
	Hangi metotla siralama yapilacagini sordurur.
	'''
	global soru
	soru = int(input('Hangi metotla siralama yapilsin? (1:SPT, 2:EDD):	'))
	if (soru == 1):
		SPTfunc()
	elif (soru == 2):
		EDDfunc()
	else:
		print('\n !!! Yanlis deger girildi. Tekrar girin. !!!\n')
		siralamafunc()
def gecikmesorufunc():
	'''
	Lateness ve tardiness hesaplanip hesaplanmayacagi sorulur.
	'''
	global gecikme
	gecikme = input('Lateness ve Tardiness hesaplansin mi? (Y/N)	')
	if (gecikme.lower() == 'y'):
		latenessfunc()
	elif (gecikme.lower() == 'n'):
		print('Gule gule')
	else:
		print('\n !!! Yanlis deger girildi. Tekrar girin. !!!\n')
		gecikmefunc()

#Program
input('IS SIRALAMA PROGRAMI\n\nBASLAMAK ICIN [ENTER] BASIN')
inputfunc()
siralamafunc()
gecikmesorufunc()
input('\nCIKMAK ICIN [ENTER] BASIN')