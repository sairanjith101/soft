binary_numbers = input("Enter a sequence of comma-separated 4-digit binary numbers: ")

binary_list = binary_numbers.split(',')

print(binary_list)

divisible_by_5 = []

for binary in binary_list:
    print(binary, end=" ")

    decimal = int(binary,2)
    print(decimal)

    if decimal % 5 == 0:
        divisible_by_5.append(binary)

print(divisible_by_5)



