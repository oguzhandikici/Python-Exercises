def unique_list(lst):
	unique=set(lst)
	uniqueList=[x for x in unique]
	print(uniqueList)
##Check
unique_list([1,1,1,1,2,2,2,3,3,3,3,3,4,5,5])