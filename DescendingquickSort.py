#Angka terakhir 8 = [ 14, 1, 4, 2, 16, 8, 5, 10, 12, 18 ]
def quickSort(arr):
    n = len(arr)
    if n <=1 :
        return arr
    left = []
    right = []
    equal = []
    pivot = arr [-1]
    for num in arr:
        if num > pivot:
            left.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            right.append(num)
    return quickSort(left)+equal + quickSort(right)
    
   
        
arrayBelumUrut = [ 14, 1, 4, 2, 16, 8, 5, 10, 12, 18 ]
print ("arrayBelumUrut", arrayBelumUrut)

arraySudahUrut = quickSort(arrayBelumUrut)
print ("arraySudahUrut", arraySudahUrut)  
                
    

