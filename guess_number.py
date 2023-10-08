import random


def user_guess():
    x = int(input('Choose a number for the maximum range: '))
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(
        f'Yay, congrats. Tou have guessed the number {random_number} correctly!')


def compututer_guess():
    x = int(input('Choose a number for the maximum range: '))
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'Is {guess} too high (H), too low (L), or correct (C)?')
        if feedback.upper() == 'H':
            high = guess - 1
        elif feedback.upper() == 'L':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!')


def select_guess():
    select = int(
        input('(1) for User Guess The Number, or (2) for Computer Guess The Number: '))
    if select == 1:
        user_guess()
    elif select == 2:
        compututer_guess()
    else:
        print("Invalid option")
        select_guess()


if __name__ == '__main__':
    select_guess()
