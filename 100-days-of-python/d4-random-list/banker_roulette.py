import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
rand_number = random.randrange(len(names))
print(f'{names[rand_number]} is going to buy the meal today!')

