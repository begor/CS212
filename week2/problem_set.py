import re
import itertools
from cryptoarithmetic import compile_word


def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
    in same order as parms of function. The first digit of a multi-digit
    number can't be 0. So if YOU is a word in the formula, and the function
    is called with Y eqal to 0, the function should return False."""

    letters = ''.join(set(re.findall('[A-Z]', formula)))
    first_letters = ','.join([c[0] for c in
                              re.findall('([A-Z]+)', formula)])
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda {}:{} and all([{}])'.format(parms, body, first_letters)
    return eval(f), letters


def faster_solve(formula):
    """
    A better algorithm for solving cryptoarithmetic tasks.

    Compiles given formula into lambda-expression only ones,
    then tries every possible permutation for params and return those,
    which evaluates to True.
    """
    f, letters = compile_formula(formula)
    for digits in itertools.permutations(range(0, 10), len(letters)):
        try:
            if f(*digits):
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ArithmeticError:
            pass


def floor_puzzle():
    """
    Hopper, Kay, Liskov, Perlis, and Ritchie live on
    different floors of a five-floor apartment building.
    Kay does not live on the bottom floor.
    Hopper does not live on the top floor.
    Liskov does not live on either the top or the bottom floor.
    Perlis lives on a higher floor than does Kay.
    Ritchie does not live on a floor adjacent to Liskov's.
    Liskov does not live on a floor adjacent to Kay's.
    """
    floor_permutations = itertools.permutations(range(1, 6))
    for (Hopper, Kay, Liskov, Perlis, Ritchie) in floor_permutations:
        if (Kay != 1 and Hopper != 5 and
            Liskov not in (1, 5) and Perlis > Kay and
            abs(Ritchie - Liskov) > 1 and abs(Liskov - Kay) > 1):
            return [Hopper, Kay, Liskov, Perlis, Ritchie]
