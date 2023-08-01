print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

both_names = (name1 + name2).lower()
true_count = 0
love_count = 0

for letters in set('true'):
    true_count += both_names.count(letters)

for letters in set('love'):
    love_count += both_names.count(letters)

total_score = int(str(true_count) + str(love_count))

if total_score < 10 or total_score > 90:
    print(f'Your score is {total_score}, you go together like coke and mentos.')
elif total_score >= 40 and total_score <= 50:
    print(f'Your score is {total_score}, you are alright together.')
else:
    print(f'Your score is {total_score}.')