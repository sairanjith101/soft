
def printAl(arr,n):
    for i in range(len(arr)):
        if n == len(arr):
            if i % 2 == 0:
                print(arr[i], end=" ")
   
# n = 5
# arr = [1,2,3,4,5]

n = 4
arr = [1,2,3,4]

printAl(arr,n)