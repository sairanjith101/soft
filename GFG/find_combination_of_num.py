from itertools import combinations

def findcombination(arr,total):
    combination_num = combinations(arr, 2)

    output = 0

    for comb in combination_num:
        if sum(comb) == total:
            output += 1
    return output

# arr = [4, 4, 5, 3]
# total = 8

arr = [-7, 1, 5, 1, 4]
total = 6

print(findcombination(arr,total))

