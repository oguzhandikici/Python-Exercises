def inputoncelikler():
	'''
	Karisik goruntu olusturdugu icin is oncelikleri bu fonksiyonla alinacak.
	'''
	class Error(Exception):
		pass
	class Error1(Error):
		pass
	class Error2(Error):
		pass
	global oncelikler
	oncelikler = []
	for i in isler:
		oncelikler.append([i,0])
	for i in range(len(isler),0,-1):
		while True:
			try:
				oncelikler[i-1][1] = (int(input('{}. isten bir once yapilmasi gereken isi girin.(Yoksa 0 girin.):  '.format(i))))
				if (oncelikler[i-1][1]==i):
					raise Error1
				elif (oncelikler[i-1][1]>len(isler)):
					raise Error2
				break
			except ValueError:
				print('Sadece tamsayi girmelisiniz. Tekrar girin.')
			except Error1:
				print('Bir isin onceligi nasil kendisi olsun? Tekrar girin.')
			except Error2:
				print('Varolan is sayisindan yuksek bir deger girdiniz. Tekrar girin.')

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
		
def RSfunc():
	'''
	Minimum Bolluk Algoritmasina gore isler siralaniyor.
	'''
	global t
	global oncelikler
	global issiralama
	global cj
	dummyisler = []
	RS = []
	issiralama = []
	cj = []
	
	#Gerçek sanat aşağıdadır.
	
	while len(issiralama)<len(isler):
		for i in range(len(oncelikler)):
			if oncelikler[i][1]==0:
				dummyisler.append(oncelikler[i][0])
			else:
				continue
		for i in range(len(dummyisler)):
			RS.append([dummyisler[i]])
			RS[i].append(ipjdj[dummyisler[i]-1][2]-ipjdj[dummyisler[i]-1][1]-t)
			
		if len(RS)==1:
			minRSidx = 0
			issiralama.append(RS[minRSidx][0])
		else:
			minRSidx = dummyisler.index(min(RS, key=lambda x: x[1])[0])
			issiralama.append(RS[minRSidx][0])
		
		t += ipjdj[issiralama[-1]-1][1]
		cj.append(t)
		
		for i in range(len(oncelikler)):
			if oncelikler[i][0]==dummyisler[minRSidx]:
				del oncelikler[i]
				break
			else:
				continue
		for i in range(len(oncelikler)): 
			if oncelikler[i][1] in issiralama:
				oncelikler[i][1]=0
			else:
				continue
		dummyisler = []
		RS = []
def tardinessfunc():
	'''
	Siralanmis islerin tardiness'lari hesaplanir.
	'''
	global tardiness
	tardiness = []
	for i in range(len(issiralama)):
		if cj[i]-ipjdj[issiralama[i]-1][2]<0:
			tardiness.append(0)
		else:
			tardiness.append(cj[i]-ipjdj[issiralama[i]-1][2])
def printfunc():
	'''
	Lazim seyler printlenir.
	'''
	print('\nMINIMUM BOLLUK ALGORITMASINA GORE IS SIRALAMA\n')
	for i in range(len(issiralama)):
		print('{}. sirada {} numarali is yapilacak.'.format(i+1,issiralama[i]))
	print('\nTARDINESS\n')
	for i in range(len(issiralama)):
		print('{}. siradaki is icin {}.'.format(i+1,tardiness[i]))
	print('\nMAKESPAN\n')
	print('{}'.format(cj[-1]))
###
print('MINIMUM BOLLUK ALGORITMASI\n')
t=0
inputfunc()
inputoncelikler()
RSfunc()
tardinessfunc()
printfunc()
input('Cikmak icin [ENTER] basin.')