# FUNCTION FOR SELECTION SORT ALGORITHM
def selection_sort_algo(listX):
	n = len(listX)
	for i in range(0, n):
		imin = i 
		for j in range(i+1, n):
			if listX[j] < listX[imin]:
				imin = j
		# STANDARD WAY TO SWAP OBJECTS IN PYTHON		
		listX[imin], listX[i] = listX [i], listX[imin]
	return listX			


list_tst = [3,4,1,9,2,11]
print(selection_sort_algo(list_tst))                
