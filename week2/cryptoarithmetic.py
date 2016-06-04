import string
import re
import itertools


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for f in fill_in(formula):
        if valid(f):
            return f


def compile_word(word):
    """
    Compile a word of uppercase letters as numeric digits.

    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'
    """
    if word.isupper():
        upper_with_order = ['{}*{}'.format(str(10**exp), digit)
                            for exp, digit in enumerate(reversed(word))]
        return '+'.join(upper_with_order)
    return word


def fill_in(formula):
    """Generate all possible fillings-in of letters in formula with digits."""
    letters = ''.join({s for s in formula if s.isalpha()})
    for digits in itertools.permutations('1234567890', len(letters)):
        table = str.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """
    Formula f is valid if and only if it has no
    numbers with leading zero, and evals true.
    """
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False
