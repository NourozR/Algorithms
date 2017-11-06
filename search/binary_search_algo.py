#FUNCTION FOR BINARY SEARCH ALGORITHM
def BinarySearchAlgo(listX, item):
	    # INITIALIZATION
	    start = 0
	    end = len(listX)-1
	    found = False
	    # MAIN LOOP
	    while start<=end and not found:
	        midpoint = (start + end)//2
	        if listX[midpoint] == item:
	            found = True
	        else:
	            if item < listX[midpoint]:
	                end = midpoint-1
	                index = end
	            else:
	                start = midpoint+1
	                index = start

	    # THIS WILL RETURN INDEX BESIDES SEARCH            
	    if found == True:
	    	return found, index
	    else:
	    	return found
	    	
# TEST LIST	                
list_t = [1,2,3,5,6,9,12,34,98]

def run:
    print(BinarySearchAlgo(list_t, 7))
    print(BinarySearchAlgo(list_t, 34))


if __name__ == '__main__':
	 run()    

