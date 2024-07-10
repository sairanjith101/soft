with open("samplefile.txt", "r") as file1:
    with open("newfile.txt", "w") as file2:
        lines = file1.readlines()
        lines.sort()
        file2.writelines(lines)
