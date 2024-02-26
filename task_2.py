import random

user_name = input('Hello! What is your name?\n')

number = random.randint(1, 40)

print(f'Well, {user_name}, I am thinking of a number between 1 and 40.')
count_of_attempts = 1

while count_of_attempts <= 10:

    try:
        guess_number = int(input('Take a guess! Enter your number: '))

        if guess_number == number:
            print(f'Good job, {user_name}! You are a winner!')
            break

        elif 1 <= guess_number <= 40 and guess_number < number:
            print('Your number is less.')

        elif 1 <= guess_number <= 40 and guess_number > number:
            print('Your number is more.')

        elif not 1 <= guess_number <= 40:
            print(f"Your number is not in the range 1 to 40. Try again:)")

    except ValueError as exception:
        print("Enter only integer numbers please!")

    count_of_attempts += 1

print("You had only 10 attempts... Game over!")