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

def tardinessfunc():
	'''
	Siralanmis islerin tardiness'lari hesaplanir.
	'''
	global tardiness
	global c
	tardiness = []
	c=[]
	t=0
	for i in range(len(acgozlu)):
		t+=ipjdj[acgozlu[i]-1][1]
		c.append(t)
	for i in range(len(acgozlu)):
		if c[i]-ipjdj[acgozlu[i]-1][2]<0:
			tardiness.append(0)
		else:
			tardiness.append(c[i]-ipjdj[acgozlu[i]-1][2])

def sontardinessfunc():
	'''
	Minimum tardiness'lı isi bulmak icin kullanilacak.
	'''
	global sontardiness
	sontardiness = []
	for i in range(len(acgozlu)-iterasyon):
		if cj[-1]-ipjdj[acgozlu[i]-1][2]<0:
			sontardiness.append(0)
		else:
			sontardiness.append(cj[-1]-ipjdj[acgozlu[i]-1][2])

def Greedyfunc():
	'''
	Acgozlu Algoritmaya gore isler siralaniyor.
	'''
	global cj
	global iterasyon
	global acgozlu
	
	iterasyon=0
	acgozlu=isler
	cj=[]
	t=0
	while iterasyon<len(acgozlu):
		for i in range(len(acgozlu)-iterasyon):
			t += ipjdj[acgozlu[i]-1][1]
			cj.append(t)

		t=0
		sontardinessfunc()
		minTidx=sontardiness.index(min(sontardiness))
		atanacak=acgozlu[minTidx]
		acgozlu.insert(len(acgozlu)-iterasyon,atanacak)
		del acgozlu[minTidx]
		
		iterasyon+=1

	tardinessfunc()

def printfunc():
	'''
	Lazim seyler printlenir.
	'''
	print('\nACGOZLU ALGORITMAYA GORE IS SIRALAMA\n')
	for i in range(len(acgozlu)):
		print('{}. sirada {} numarali is yapilacak.'.format(i+1,acgozlu[i]))
	print('\nTARDINESS\n')
	for i in range(len(acgozlu)):
		print('{}. siradaki is icin {}.'.format(i+1,tardiness[i]))
	print('\nMAKESPAN\n')
	print('{}'.format(c[-1]))
###
print('ACGOZLU ALGORITMA\n')
inputfunc()
Greedyfunc()
printfunc()
input('Cikmak icin [ENTER] basin.')