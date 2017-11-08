# FUNCTION FOR MERGING TWO LIST
def merge(L, R):
	empty = []
	nL = len(L)
	nR = len(R)
	i, j = 0, 0
	# THIS WILL SORT
	while (i < nL and j < nR):
		if L[i] <= R[j]:
			empty.append(L[i])
			i = i+1
		else:
			empty.append(R[j])
			j = j+1
	# THIS WILL APPEND THE LEFT VALUES		
	for i in range(i, nL):
		empty.append(L[i])

	for j in range(j, nR):
		empty.append(R[j])

	return empty	
			
# FUNCTION FOR MERGE SORT ALGORITHM
def MergeSort(listX):
		if len(listX) < 2:
			return listX
		else:	
		    mid = len(listX) // 2
		    L, R = MergeSort(listX[:mid]), MergeSort(listX[mid:])
		    return merge(L, R)	

list_test = [7,3,0,23,12,11,31,19,18,17,1]	
print MergeSort(list_test)	

			