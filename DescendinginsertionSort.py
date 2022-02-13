#Angka terakhir 8 = [ 14, 1, 4, 2, 16, 8, 5, 10, 12, 18 ]
def insertionSort(arr):
   
    for i in range(1, len(arr)):
        nilaiYangSedangDicek = arr[i]
       
        while arr[i-1] < nilaiYangSedangDicek and i > 0  :
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i = i-1
            
    return arr
        
arrayBelumUrut = [ 14, 1, 4, 2, 16, 8, 5, 10, 12, 18 ]
print ("arrayBelumUrut", arrayBelumUrut)

arraySudahUrut = insertionSort(arrayBelumUrut)
print ("arraySudahUrut", arraySudahUrut)                
                
    

