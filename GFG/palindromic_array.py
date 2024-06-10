


def PalinArray(arr ,n):
    if n == len(arr):
        global d
        d = 0
        for i in arr:
            z = str(i)
            if z == z[::-1]:
                d += 1
            else:
                pass
    

n = 5

arr = [111, 222, 333, 444, 555]

PalinArray(arr, n)

if d == len(arr):
    print(1)
else:
    print(0)



