##Kure hacmi
from math import pi
def vol(rad):
	return 4/3*pi*rad**3
##Check
result=vol(int(input('Yaricap girin:  ')))
print('{} br^2'.format(round(result,1)))