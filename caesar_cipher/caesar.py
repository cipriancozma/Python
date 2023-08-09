from logo import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction):
    newString = ''

    for letter in text:
        if shift > 26:
            shift = shift % alphabet.index(letter)
        else:
            if letter not in alphabet:
                newString += letter
            else:
                oldString = alphabet.index(letter)
                if direction == 'encode':
                    newStringIdx = oldString + shift
                elif direction == 'decode':
                    newStringIdx = oldString - shift
                newString += alphabet[newStringIdx]

    print(f"The {'encoded' if direction == 'encode' else 'decoded'} text is {newString}")


caesar(text, shift, direction)

user_response = input("Do you want to restart the program?")

while user_response == 'yes':
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    user_response = input("Do you want to restart the program?")
