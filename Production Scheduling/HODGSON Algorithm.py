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

def tardinessfunc():
	'''
	Tardiness hesaplanir. Sadece HODGSON'da kullanilabilir formda.
	'''
	global tardiness
	tardiness = []
	cj = []
	t = 0

	for i in range(len(isler)):
		t += Hsiralama[i][1]
		cj.append(t)
	for i in range(len(isler)):
		if cj[i]-Hsiralama[i][2]<0:
			tardiness.append(0)
		else:
			tardiness.append(cj[i]-Hsiralama[i][2])

def hodgsonfunc():
	'''
	Hodgson Algoritmasi uygulanarak is siralamasi yapilir.
	'''
	global Hsiralama
	global dummy

	tardinesscount = []
	dokunulmaz = []
	iterasyon = 0
	
	Hsiralama = sorted(ipjdj, key=lambda x: x[2])
	
	tardinessfunc()

	for i in range(len(isler)+1):
		tardinesscount.append([])
	for i in range(len(tardiness)):
		if tardiness[i]>0:
			tardinesscount[iterasyon].append(1)

	while (sum(tardiness) > 0) and (iterasyon < len(isler)): 
		dummy = []
		for i in range(len(isler)):
			if (tardiness[i]==0):
				dummy.append(Hsiralama[i])
			elif (tardiness[i]>0):
				dummy.append(Hsiralama[i])
				if len(dummy)==1:
					dummyindex=0
					dummyis=dummy[dummyindex][0]
				else:
					dummyindex = dummy.index(max(dummy, key=lambda x: x[1]))
					dummyis=dummy[dummyindex][0]
				break

		if (iterasyon > 0) and (dummyis in dokunulmaz): 
			break

		del Hsiralama[dummyindex]
		Hsiralama.append(dummy[dummyindex])
		dokunulmaz.append(Hsiralama[-1][0])
		tardinessfunc()

		for i in range(0,len(tardiness)): 
			if (tardiness[i] > 0):
				tardinesscount[iterasyon+1].append(1)

		if (sum(tardinesscount[iterasyon]) < sum(tardinesscount[iterasyon+1])) and (tardiness[-1]>0):
			del Hsiralama[-1]
			Hsiralama.insert(dummyindex, dummy[dummyindex])
			tardinessfunc()
			break
		iterasyon += 1

	print('\nHODGSON COZUM\n')
	for i in range(0,len(isler)):
		print('{}. sirada {} numarali is yapilacak.'.format(i+1,Hsiralama[i][0]))
	print('\nTARDINESS\n')
	for i in range(0,len(isler)):
		print('{}. siradaki is icin {}'.format(i+1,tardiness[i]))

#####
input('HODGSON ALGORITMASI\n\nBASLAMAK ICIN [ENTER] BASIN')
inputfunc()
hodgsonfunc()
input('\nCIKMAK ICIN [ENTER] BASIN')