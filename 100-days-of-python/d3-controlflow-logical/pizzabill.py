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

if size == 'S':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            final_bill = small + pepperoni_small + add_cheese
            print(f'Your final bill is: ${final_bill}.')
        else:
            final_bill = small + pepperoni_small
            print(f'Your final bill is: ${final_bill}.')
    else:
        if extra_cheese == 'Y':
            final_bill = small + add_cheese
            print(f'Your final bill is: ${final_bill}.')
        else:
            final_bill = small
            print(f'Your final bill is: ${final_bill}.')
            
elif size == 'M':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            final_bill = medium + pepperoni_large_medium + add_cheese
            print(f'Your final bill is: ${final_bill}.')
        else:
            final_bill = medium + pepperoni_large_medium
            print(f'Your final bill is: ${final_bill}.')
    else:
        if extra_cheese == 'Y':
            final_bill = medium + add_cheese
            print(f'Your final bill is: ${final_bill}.')
        else:
            final_bill = medium
            print(f'Your final bill is: ${final_bill}.')
            
elif size == 'L':
    if add_pepperoni == 'Y':
        if extra_cheese == 'Y':
            final_bill = large + pepperoni_large_medium + add_cheese
            print(f'Your final bill is: ${final_bill}.')
        else:
            final_bill = large + pepperoni_large_medium
            print(f'Your final bill is: ${final_bill}.')
    else:
        if extra_cheese == 'Y':
            final_bill = large + add_cheese
            print(f'Your final bill is: ${final_bill}.')
        else:
            final_bill = large
            print(f'Your final bill is: ${final_bill}.')
else:
    print('Invalid Input')