with open('sample.txt', 'r') as file1, open('newfile.txt', 'w') as file2:
    for line in file1:
        if 'melon' in line.lower():
            file2.write(line)