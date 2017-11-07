# FUNTION FOR INSERTION SORT
def InsertionSort(listX):
	n = len(listX)
	for i in range(1, n):
		val = listX[i]
		hole = i
		while(hole > 0 and listX[hole-1] > val):
			listX[hole] = listX[hole-1]
			hole = hole-1
		listX[hole] = val 
	return listX

# TEST THE ALGORITHM WITH A LIST
list_tst = [2,6,8,1,4,5,21,3,12]
print(InsertionSort(list_tst))			