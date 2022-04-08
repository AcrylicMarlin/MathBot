import math
import operator
import random

from enum import Enum

class Operators(Enum):
    ADD = operator.add
    SUB = operator.sub
    MUL = operator.mul
    DIV = operator.truediv
    POW = operator.pow


def start_review():
    """
    Starts the math facts review
    """
    options = {
        'multiply': multi_review,
        'divide': div_review,
        'subtract': sub_review,
        'add': add_review,
        'power': pow_review
    }
    options[input('What would you like to review?').lower()]()

def multi_review():
    limit = int(input('How many questions would you like to review?'))
    num_wrong = 0
    num_right = 0
    while (True):
        x = random.randint(1, 12)
        y = random.randint(1, 12)
        fact = '{} x {} = What?'.format(x, y)

        answer = int(input(fact))
        if answer != x * y:
            num_wrong += 1
            print('Wrong!')
        else:
            num_right += 1
            print('Correct!')
        
        if num_wrong + num_right == limit:
            break
    
    print('You got {} right and {} wrong'.format(num_right, num_wrong))
    print('Good job!' if num_right > num_wrong else 'You need to study more.')

    ...
def div_review():
    ...
def sub_review():
    ...
def add_review():
    ...
def pow_review():
    ...
