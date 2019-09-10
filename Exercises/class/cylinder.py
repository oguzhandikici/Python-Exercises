class Cylinder:

	pi=3.1415

	def __init__(self,r,h):
		self.radius=r
		self.height=h

	def volume(self):
		return Cylinder.pi*self.height*self.radius**2

	def surface_area(self):
		circle=Cylinder.pi*self.radius**2
		return (2*circle)+(2*Cylinder.pi*self.radius*self.height)
##Check
r=float(input('Yaricap girin:  '))
h=float(input('Yukseklik girin:  '))
cyl=Cylinder(r,h)
vol=cyl.volume()
surfArea=cyl.surface_area()
print('Silindir hacmi = {}'.format(round(vol,2)))
print('Silindir yuzey alani = {}'.format(round(surfArea,2)))