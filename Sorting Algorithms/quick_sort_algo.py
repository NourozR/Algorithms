# FUNCTION FOR MAKING THE PARTITION THROUGH PIVOT
def Partition(listX, start, end):
	pivot = end 
	pIndex = start
	for i in range(start, end):
		if listX[i] <= listX[pivot]:
			# SWAP
			listX[i], listX[pIndex] = listX[pIndex], listX[i]
			pIndex = pIndex+1
	# SWAP		
	listX[pIndex], listX[end] = listX[end], listX[pIndex]	
	return pIndex

# FUNCTION FOR QUICK SORT ALGORITHM	
def QuickSort(listX, start, end):
	
	if start < end:
		pIndex = Partition(listX, start, end)
		# RECURSION
		QuickSort(listX, start, pIndex-1)
		QuickSort(listX, pIndex+1, end)
		return listX
	else:
		return listX

# TEST THE ALGORITHM WITH A LIST
list_test = [1,5,65,-1,-5,-2,242,100,4,423,0,10,43,64]		
print(QuickSort(list_test, start=0, end=len(list_test)-1))
		

