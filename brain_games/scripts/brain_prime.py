#!/usr/bin/env python3

import prompt
from random import randint


def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True



def game(name, counter):
    number = randint(1, 3600)
    print('Question: ', number)
    answer = prompt.string('Your answer: ')
    result = is_prime(number)

    if answer == 'yes':
        if result:
            print('Correct!')
            counter += 1
            return counter
        print(f'\'yes\' is wrong answer ;(. Correct answer was \'no\'.')
        print(f'Let\'s try again, {name}!')
        counter = 0
        return counter
    elif answer == 'no':
        if not result:
            print('Correct!')
            counter += 1
            return counter
        print(f'\'no\' is wrong answer ;(. Correct answer was \'yes\'.')
        print(f'Let\'s try again, {name}!')
        counter = 0
        return counter
    else:
        print('This is wrong answer!')
        counter = 0
        return counter


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(f'Answer "yes" if given number is prime. Otherwise answer "no".')
    counter = 0
    while counter < 3:
        counter = game(name, counter)
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
