def remove_common_characters(name1, name2):
    for char in name1[:]:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    return name1, name2

def flames_count(name1, name2):
    name1, name2 = remove_common_characters(name1, name2)
    return len(name1 + name2)

def flames_result(count):
    flames = ['F', 'L', 'A', 'M', 'E', 'S']
    while len(flames) > 1:
        split_index = (count % len(flames)) - 1
        if split_index >= 0:
            flames = flames[split_index + 1:] + flames[:split_index]
        else:
            flames = flames[:len(flames) - 1]
    return flames[0]

def flames_relationship(letter):
    relationships = {
        'F': 'Friends',
        'L': 'Love',
        'A': 'Affection',
        'M': 'Marriage',
        'E': 'Enemies',
        'S': 'Siblings'
    }
    return relationships[letter]

def main():
    user1 = input("Enter the first name: ").lower().replace(" ", "")
    user2 = input("Enter the second name: ").lower().replace(" ", "")

    count = flames_count(user1, user2)
    result_letter = flames_result(count)
    result = flames_relationship(result_letter)

    print(f"The relationship between {user1} and {user2} is: {result}")

if __name__ == "__main__":
    main()
