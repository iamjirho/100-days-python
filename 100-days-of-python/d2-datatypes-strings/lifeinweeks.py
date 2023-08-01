age = input("What is your current age? ")

age_int = int(age)
remaining_years = 90 - age_int

convert_to_days = remaining_years * 365
convert_to_weeks = remaining_years * 52
convert_to_months = remaining_years * 12

print(f'You have {convert_to_days} days, {convert_to_weeks} weeks, and {convert_to_months} months left.')