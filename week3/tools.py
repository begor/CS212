from functools import wraps, update_wrapper


def decorator(d):
    """Makes function a decorator by copying its inner attribs."""
    return lambda fn: update_wrapper(d(fn), fn)


decorator = decorator(decorator)


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
