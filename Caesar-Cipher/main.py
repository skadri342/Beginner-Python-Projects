from art import logo

print(logo)
end = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):                         # combining the previous two functions into one 
    end_text = ""
    if direction == "decode":
        shift *= -1
    for char in text:
        if char in alphabet: 
            position = alphabet.index(char)
            new_position = position + shift
            if new_position >= 0:                               # This gets the new letter with the shift number added, we are using the modulo operator for when the index is out
                new_letter = alphabet[new_position % 26]        # of range then it will loop back to the start of the index range and keep on going
            else:
                new_letter = alphabet[new_position % 26 - 26]   
            end_text += new_letter                              # Adds each of the encrypted letter to a new string, have to remember that you can add to a string just like a list.
        else:
            end_text += char
    print(f"The {direction}d text is {end_text}")
        
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type any other character.\n")
    if not restart == "yes":
        end = True
        print("Goodbye")

# while not end:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt or anything else to exit:\n").lower()
    
#     def encrypt(text, shift):
#         cipher_text = ""
        
#         for letter in text:
#             position = alphabet.index(letter)                   # Gets the index number of the current letter in the for loop of the text               
#             new_position = position + shift                     # Shifts the index number by the shift number
#             if new_position >= 0:                               # This gets the new letter with the shift number added, we are using the modulo operator for when the index is out
#                 new_letter = alphabet[new_position % 26]        # of range then it will loop back to the start of the index range and keep on going
#             else:
#                 new_letter = alphabet[new_position % 26 - 26]   
#             cipher_text += new_letter                           # Adds each of the encrypted letter to a new string, have to remember that you can add to a string just like a list.
#         print(f"The encoded text is {cipher_text}")

#     def decrypt(text, shift):
#         plain_text = ""
        
#         for letter in text:
#             position = alphabet.index(letter)                                 
#             new_position = position - shift
#             if new_position >= 0:                               
#                 new_letter = alphabet[new_position % 26]        
#             else:
#                 new_letter = alphabet[new_position % 26 - 26]
#             plain_text += new_letter
#         print(f"The decoded text is {plain_text}")

#     if direction == "encode":
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         encrypt(text, shift)
#     elif direction == "decode":
#         text = input("Type your message:\n").lower()
#         shift = int(input("Type the shift number:\n"))
#         decrypt(text, shift)
#     else:
#         print("Exiting the program")
#         end = True