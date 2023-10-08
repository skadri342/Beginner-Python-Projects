#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 
           'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', '@']

print("Welcome to the Password Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Choose letters randomly:
#have to randomise how many times based on number of letters
random_letters = []
for number_of_letters in range(0, nr_letters):
    random_choice = random.randint(0, len(letters) - 1) #can also use random.choice() method.
    random_letters.append(letters[random_choice])

# print(random_letters)  
#Choose symbols randomly:
random_symbols = []
for number_of_letters in range(0, nr_symbols):
    random_choice = random.randint(0, len(symbols) - 1) #can also use random.choice() method.
    random_symbols.append(symbols[random_choice])

#Choost numbers randomly:
random_numbers = []
for number_of_numbers in range(0, nr_numbers):
    random_choice = random.randint(0, len(numbers) - 1) #can also use random.choice() method.
    random_numbers.append(numbers[random_choice])
    
#Choose the order to display the 3 above randomly:
password = []
password.append(random_letters)
password.append(random_numbers)
password.append(random_symbols)

#turns the nested list into a list
random_p = []
for element in password:
    if type(element) is list:
        for item in element:
            random_p.append(item)
    else:
        random_p.append(element)
        
random.shuffle(random_p)

random_password = ''
for element in random_p:
    random_password += element    

print(random_password)    