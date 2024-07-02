def findnum(vowels, spaces, user):
    lower_user = user.lower()

    vowels_count = 0
    consonants_count = 0
    spaces_count = 0

    for i in lower_user:
        if i in vowels:
            vowels_count += 1
        elif i.isalpha():  # Ensure consonants are only alphabetic characters
            consonants_count += 1
    
        if i in spaces:
            spaces_count += 1

    return vowels_count, consonants_count, spaces_count

vowels = ['a', 'e', 'i', 'o', 'u']
spaces = [" "]
user = "Ranjith kumar"

print(findnum(vowels, spaces, user))
