#!/usr/bin/env python3

import prompt
from random import randint, choice


def generate_expression():
    operators = ['+', '-', '*']
    num1 = randint(1, 50)
    num2 = randint(1, 20)
    operator = choice(operators)
    expression = f'{num1} {operator} {num2}'
    return expression


def is_calc(name, counter):
    random_exp = generate_expression()
    print(f'Question: {random_exp}')
    answer = eval(prompt.string('Your answer: '))
    result = eval(random_exp)

    if answer == result:
        print('Correct!')
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
    print(f'What is the result of the expression?')
    counter = 0
    while counter < 3:
        counter = is_calc(name, counter)
    print(f'Congratulations, {name}!')


if __name__ == "__main__":
    main()
