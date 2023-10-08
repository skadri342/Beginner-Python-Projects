# Write your code below this line 👇
def prime_checker(number): 
    products = 0    
    for divisors in range(1, number+1):
        if number % divisors == 0:
            products += 1
        
    if number <= 1:
        print("It's not a prime number.")    
    elif products == 2:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")           
# Write your code above this line 👆
# Prime number is a number greater than 1 that can be only divided by itself and 1. 
    
#Do NOT change any of the code below👇
n = int(input("What number do you want to check: ")) # Check this number
prime_checker(number=n)