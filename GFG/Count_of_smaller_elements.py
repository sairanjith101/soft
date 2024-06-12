n = 6
a = [1, 2, 4, 5, 8, 10]
x = 9

def countOfElements(a, n, x):
    res = 0
    for i in a:
        if len(a) == n:
            if i <= x:
                res += 1
    return res

print(countOfElements(a,n,x))