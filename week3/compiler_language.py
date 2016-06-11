def match(pattern, text):
    "Match pattern against start of text; return longest match found or None."
    remainders = pattern(text)
    if remainders:
        shortest = min(remainders, key=len)
        return text[:len(text) - len(shortest)]


def lit(s):
    return lambda text: set([text[len(s):]]) if text.startswith(s) else null


def seq(x, y):
    return lambda text: set().union(*map(y, x(text)))


def alt(x, y):
    return lambda text: x(text) | y(text)


def oneof(chars):
    return lambda text: set([text[1:]]) if (text and text[0] in chars) else null


def plus(x):
    return seq(x, star(x))


def star(x):
    return lambda text: (set([text]) |
                         set(t2 for t1 in x(text) if t1 != text
                             for t2 in star(x)(t1)))


dot = lambda text: set([text[1:]]) if text else null


eol = lambda text: set(['']) if text == '' else null


null = frozenset([])


def test():
    assert match(star(lit('a')), 'aaaaabbbaa') == 'aaaaa'
    assert match(lit('hello'), 'hello how are you?') == 'hello'
    assert match(lit('x'), 'hello how are you?') == None
    assert match(oneof('xyz'), 'x**2 + y**2 = r**2') == 'x'
    assert match(oneof('xyz'), '   x is here!') == None
    return 'tests pass'

print(test())
