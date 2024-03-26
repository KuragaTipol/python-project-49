#!/usr/bin/env python3

import prompt
from random import randint


def is_even(name, counter):
    rand = randint(1, 99)
    print(f'Question: {rand}')
    answer = prompt.string('Your answer: ')
    if rand % 2 == 0:
        if answer == 'yes':
            print('Correct!')
            counter += 1
            return counter
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'yes\'.')
            print(f'Let\'s try again, {name}!')
            exit()
    else:
        if answer == 'no':
            print('Correct!')
            counter += 1
            return counter
        else:
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'no\'.')
            print(f'Let\'s try again, {name}!')
            exit()


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(f'Answer "yes" if the number is even, otherwise answer "no".')
    counter = 0
    while counter < 3:
        counter = is_even(name, counter)
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
