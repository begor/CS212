from functools import wraps, update_wrapper


def decorator(d):
    """Makes function a decorator by copying its inner attribs."""
    def _d(fn):
        return update_wrapper(d(fn), fn)
    update_wrapper(_d, d)
    return _d
    # or: return lambda fn: update_wrapper(d(fn), fn)
    # and: decorator = decorator(decorator)


@decorator
def n_ary(f):
    """Given binary function f(x, y), return an n_ary function such
    that f(x, y, z) = f(x, f(y,z)), etc. Also allow f(x) = x."""
    @wraps(f)
    def n_ary_f(x, *args):
        return x if not args else f(x, n_ary_f(*args))
    return n_ary_f


@decorator
def memo(fn):
    """Memoization decorator."""
    cache = {}

    def _f(*args):
        try:
            return cache[args]
        except KeyError:
            cache[args] = result = fn(*args)
            return result
        except TypeError:  # in the case that args is unhashable
            return _f(*args)
    return _f


callcounts = {}


@decorator
def countcalls(fn):
    def _f(*args):
        callcounts[_f] += 1
        return fn(*args)
    callcounts[_f] = 0
    return _f


@decorator
def trace(f):
    indent = '   '

    def _f(*args):
        signature = '{}({})'.format(f.__name__, ', '.join(map(repr, args)))
        print('{}--> {}'.format(trace.level * indent, signature))
        trace.level += 1
        try:
            result = f(*args)
            print('{}<-- {} == {}'.format((trace.level - 1) * indent,
                                          signature, result))
        finally:
            trace.level -= 1

        return result
    trace.level = 0
    return _f


def disabled(f):
    return f


trace = disabled


@trace
def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
