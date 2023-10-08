print("Welcome to the tip calculator")
total = float(input("What was the total bill? $"))
tip_percentage = int(input("What percentage tip would you like to give? "))/100 + 1
people = int(input("How many people to split the bill? "))

result = round(total*tip_percentage/people, 2)

print(f"Each person should pay: ${result}")