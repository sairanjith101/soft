


def printPat(n):
    result = []
    for i in range(n, 0, -1):
        row = []
        for j in range(n, 0, -1):
            row.extend([j] * i)
        result.append(' '.join(map(str, row)) + ' $')
    # Join the rows without adding any extra spaces
    final_result = ''.join(result).strip()
    print(final_result)

# Test with input 2
printPat(3)




