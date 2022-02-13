#tugas descending, Angka terakhir 8 = [ 14, 1, 4, 2, 16, 8, 5, 10, 12, 18 ]
def bubbleSort(arr):
    lanjut = True
    while lanjut:
        lanjut = False
        for i in range(0, len(arr)-1):
            if arr[i] < arr[i + 1]:
                nilailebihBesar = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = nilailebihBesar
                lanjut = True
    return arr
arrayBelumUrut = [ 14, 1, 4, 2, 16, 8, 5, 10, 12, 18 ]
print ("arrayBelumUrut", arrayBelumUrut)

arraySudahUrut = bubbleSort(arrayBelumUrut)
print ("arraySudahUrut", arraySudahUrut)                
                
    

