#!/usr/bin/env python3

from brain_games.cli import welcome_user


# import prompt

# def welcome_user():
#    name = prompt.string('May I have your name? ')
#    print('Hello, {}!'.format(name))

def main():
    print('Welcome to the Brain Games!')
    welcome_user()


if __name__ == "__main__":
    main()
