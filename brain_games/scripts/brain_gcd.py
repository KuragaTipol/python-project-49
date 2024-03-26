#!/usr/bin/env python3

import prompt
from random import randint


def nod(a, b):
    while b:
        a, b = b, a % b
    return str(a)


def gcd(name, counter):
    num1 = randint(1, 50)
    num2 = randint(1, 20)
    print(f'Question: {num1} {num2}')
    answer = prompt.string('Your answer: ')
    result = nod(num1, num2)

    if answer == result:
        print("Correct!")
        counter += 1
        return counter
    else:
        print(f'\'{answer}\' is wrong answer ;(. '
              f'Correct answer was \'{result}\'.')
        print(f'Let\'s try again, {name}!')
        exit()


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print('Find the greatest common divisor of given numbers.')
    counter = 0
    while counter < 3:
        counter = gcd(name, counter)
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
