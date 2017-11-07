#FUNCTION FOR BUBBLE SORT
def bubble_sort_algo(listX):
    n = len(listX)
    for i in range(0, n - 1):
        for j in range(0, n - 2):
            if listX[j] > listX[j+1]:
                # PYTHONIC WAY TO SWAP OBJECTS
                listX[j], listX[j+1] = listX[j+1], listX[j]
    return listX            

# TEST THE ALGORITHM ON A LIST
list_tst = [3,4,5,1,8,2,0,13,9,21]
print(bubble_sort_algo(list_tst))