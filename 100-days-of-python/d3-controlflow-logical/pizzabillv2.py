print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N:  ")
extra_cheese = input("Do you want extra cheese? Y or N:  ")

small = 15
medium = 20
large = 25
pepperoni_small = 2
pepperoni_large_medium = 3
add_cheese = 1
bill = 0

if size == 'S':
    bill += small
elif size == 'M':
    bill += medium
else:
    bill += large

if add_pepperoni == 'Y':
    if size == 'S':
        bill += pepperoni_small
    else:
        bill += pepperoni_large_medium

if extra_cheese == 'Y':
    bill += add_cheese

print(f'Your final bill is: ${bill}.')
