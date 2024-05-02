import random 
random_number = random.randint(1, 100)
count_number = 0 
print("Welcome to my mini game RandomFind")
print("Game instructions:\n 1. A random number generates from 1 to 100.\n 2. You have to guess the number by using hints\n 3. Enter your guessed number in console and it will show you if you are right\n Good Luck!!")
while True:
    # Asking User the Number
    user_input = input("Enter your guessed number: ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Oops retry, please read the insturctions!")
        continue
    count_number += 1
    # Checking the number
    if user_input < random_number:
        print("Your number is lower, try again!")
    elif user_input > random_number:
        print("Your number is higher, try again!")
    else:
        print(f"Congratulations!!!\n You have guessed the number in {count_number} tries")
        break
    # Hints Part
    if abs(user_input - random_number) <= 5:
        print(f"You are so close to guess right!{random_number}")
    elif abs(user_input - random_number) <= 10:
        print("You are close to guess it right!")
    elif abs(user_input - random_number) <= 20:
        print("You are almost there!")
    elif abs(user_input - random_number) <= 30:
        print("You are slightly there!")
    elif abs(user_input - random_number) <= 50:
        print("It's too much,try again smaller number")