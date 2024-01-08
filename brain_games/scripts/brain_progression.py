#!/usr/bin/env python3

import prompt
from random import randint


def generate_progression():
    first_term = randint(1, 50)
    difference = randint(1, 6)
    progression = [first_term + i * difference for i in range(10)]
    return progression


def game(name, counter):
    progression = generate_progression()
    num = randint(0, 9)
    result = progression[num]
    progression[num] = '..'
    print('Question:', ' '.join(map(str, progression)))
    answer = eval(prompt.string('Your answer: '))

    if answer == result:
        print("Correct!")
        counter += 1
        return counter
    else:
        print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{result}\'.')
        print(f'Let\'s try again, {name}!')
        counter = 0
        return counter


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print('Hello, {}!'.format(name))
    print(f'What number is missing in the progression?')
    counter = 0
    while counter < 3:
        counter = game(name, counter)
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
