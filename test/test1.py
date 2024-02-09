letter = ['a','d','j','p','q','r']


def main():
    for i in range(len(letter)):
        if letter[0] and letter[-1]:
            letter.reverse(letter[-1])