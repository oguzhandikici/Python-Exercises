coordinate1=tuple(int(input('1. nokta icin {} koordinatini girin.'.format(coor))) for coor in ['x','y'])
coordinate2=tuple(int(input('2. nokta icin {} koordinatini girin.'.format(coor))) for coor in ['x','y'])

class Line:

	def __init__(self,coor1,coor2):
		self.coor1=coor1
		self.coor2=coor2

	def distance(self):
		return ((self.coor2[0]-self.coor1[0])**2+(self.coor2[1]-self.coor1[1])**2)**0.5

	def slope(self):
		return (self.coor2[1]-self.coor1[1])/((self.coor2[0]-self.coor1[0]))
##Check
li=Line(coordinate1,coordinate2)
dist=li.distance()
slop=li.slope()
print(dist)
print(slop)