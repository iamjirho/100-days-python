print("Welcome to the tip calculator")

bill = float(input('What was the total bill? $'))
tip_percentage = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
split = int(input('How many people to split the bill? '))

percent_to_decimal = (tip_percentage/100) + 1
payment_per_split = (bill / split) * percent_to_decimal
payment_rounded = format(payment_per_split, '.2f')

print(f'Each person should pay: ${payment_rounded}')
