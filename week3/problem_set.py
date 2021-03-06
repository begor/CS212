from functools import update_wrapper
import re

"""
1. JSON Parse.
"""

def grammar(description, whitespace=r'\s*'):
    """Convert a description to a grammar.  Each line is a rule for a
    non-terminal symbol; it looks like this:
        Symbol =>  A1 A2 ... | B1 B2 ... | C1 C2 ...
    where the right-hand side is one or more alternatives, separated by
    the '|' sign.  Each alternative is a sequence of atoms, separated by
    spaces.  An atom is either a symbol on some left-hand side, or it is
    a regular expression that will be passed to re.match to match a token.

    Notation for *, +, or ? not allowed in a rule alternative (but ok
    within a token). Use '\' to continue long lines.  You must include spaces
    or tabs around '=>' and '|'. That's within the grammar description itself.
    The grammar that gets defined allows whitespace between tokens by default;
    specify '' as the second argument to grammar() to disallow this (or supply
    any regular expression to describe allowable whitespace between tokens)."""
    G = {' ': whitespace}
    description = description.replace('\t', ' ') # no tabs!
    for line in str.split(description, '\n'):
        lhs, rhs = str.split(line, ' => ', 1)
        alternatives = str.split(rhs, ' | ')
        G[lhs] = tuple(map(str.split, alternatives))
    return G


def decorator(d):
    "Make function d a decorator: d wraps a function fn."
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d


@decorator
def memo(f):
    """Decorator that caches the return value for each call to f(args).
    Then when called again with same args, we can just look it up."""
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = f(*args)
            return result
        except TypeError:
            # some element of args can't be a dict key
            return f(args)
    return _f


def parse(start_symbol, text, grammar):
    """Example call: parse('Exp', '3*x + b', G).
    Returns a (tree, remainder) pair. If remainder is '', it parsed the whole
    string. Failure iff remainder is None. This is a deterministic PEG parser,
    so rule order (left-to-right) matters. Do 'E => T op E | T', putting the
    longest parse first; don't do 'E => T | T op E'
    Also, no left recursion allowed: don't do 'E => E op T'"""

    tokenizer = grammar[' '] + '(%s)'

    def parse_sequence(sequence, text):
        result = []
        for atom in sequence:
            tree, text = parse_atom(atom, text)
            if text is None: return Fail
            result.append(tree)
        return result, text

    @memo
    def parse_atom(atom, text):
        if atom in grammar:
            for alternative in grammar[atom]:
                tree, rem = parse_sequence(alternative, text)
                if rem is not None: return [atom]+tree, rem  
            return Fail
        else:  # Terminal: match characters against start of text
            m = re.match(tokenizer % atom, text)
            return Fail if (not m) else (m.group(1), text[m.end():])

    # Body of parse:
    return parse_atom(start_symbol, text)

Fail = (None, None)

JSON = grammar(
r"""value => string | number | object | array | true | false | null
pair => string : value
string => "[^"]*"
object => { } | { members }
array => [[] []] | [[] elements []]
elements => value , elements | value
members => pair , members | pair
number => int frac exp | int exp | int frac | int
int => -?[1-9][0-9]*
frac => [.][0-9]+
exp => [eE][+-]?[0-9]+""",
    whitespace='\s*')


def json_parse(text):
    return parse('value', text, JSON)


"""
2. Inverse function.
"""

def inverse(f, delta = 1/128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def find_bounds(x, y):
        """Find bounds in which f(x) equals y."""
        while f(x) < y:
            x *= 2
        return 0 if x == 1 else x / 2, x

    def search_btw_bounds(lo, hi, y):
        """Search a value y between bounds lo and hi."""
        while lo <= hi:
            x = (lo + hi) / 2
            if f(x) < y:
                lo += delta
            elif f(x) > y:
                hi -= delta
            else:
                return x

        return hi if (f(hi)-y < y-f(lo)) else lo

    def f_1(y):
        x = 1
        lo, hi = find_bounds(x, y)
        return search_btw_bounds(lo, hi, y)
    return f_1 


"""
3. Find HTML tags.
"""
import re

def findtags(text):
    pattern = r"<\s*[a-z]+[^>'/]*>"
    match = re.findall(pattern, text)
    return match



"""
Test suite for Problem set 3.
"""
def test():
    def test_json():
        assert json_parse('["testing", 1, 2, 3]') == (                      
                           ['value', ['array', '[', ['elements', ['value', 
                           ['string', '"testing"']], ',', ['elements', ['value', ['number', 
                           ['int', '1']]], ',', ['elements', ['value', ['number', 
                           ['int', '2']]], ',', ['elements', ['value', ['number', 
                           ['int', '3']]]]]]], ']']], '')

        assert json_parse('-123.456e+789') == (
                           ['value', ['number', ['int', '-123'], ['frac', '.456'], ['exp', 'e+789']]], '')

        assert json_parse('{"age": 21, "state":"CO","occupation":"rides the rodeo"}') == (
                          ['value', ['object', '{', ['members', ['pair', ['string', '"age"'], 
                           ':', ['value', ['number', ['int', '21']]]], ',', ['members', 
                          ['pair', ['string', '"state"'], ':', ['value', ['string', '"CO"']]], 
                          ',', ['members', ['pair', ['string', '"occupation"'], ':', 
                          ['value', ['string', '"rides the rodeo"']]]]]], '}']], '')

    def test_inverse():
        sqr = lambda x: x * x
        sqrt = inverse(sqr)
        assert sqrt(16) == 4
        assert sqrt(100) == 10
        assert sqrt(1000000) == 1000

        pow_of_10 = lambda x: 10 ** x
        inv = inverse(pow_of_10)
        assert inv(10) == 1
        assert inv(100) == 2
        assert inv(10000000000) == 10

    def test_tags():

        testtext1 = """
        My favorite website in the world is probably 
        <a href="www.udacity.com">Udacity</a>. If you want 
        that link to open in a <b>new tab</b> by default, you should
        write <a href="www.udacity.com"target="_blank">Udacity</a>
        instead!
        """

        testtext2 = """
        Okay, so you passed the first test case. <let's see> how you 
        handle this one. Did you know that 2 < 3 should return True? 
        So should 3 > 2. But 2 > 3 is always False.
        """

        testtext3 = """
        It's not common, but we can put a LOT of whitespace into 
        our HTML tags. For example, we can make something bold by
        doing <         b           > this <   /b    >, Though I 
        don't know why you would ever want to.
        """
        assert findtags(testtext1) == ['<a href="www.udacity.com">', 
                                       '<b>', 
                                       '<a href="www.udacity.com"target="_blank">']
        assert findtags(testtext2) == []
        assert findtags(testtext3) == ['<         b           >']

    test_json()
    test_inverse()
    test_tags()
    return 'tests pass'

print(test())
