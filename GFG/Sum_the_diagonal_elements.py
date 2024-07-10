arr = [
[1,2,3,4],
[5,6,7,8],
[1,2,3,4],
[5,6,7,8]
]

output = 0

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            output += arr[i][j]

print(output)