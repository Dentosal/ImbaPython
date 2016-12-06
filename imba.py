from forbiddenfruit import curse as improve
import sys
from functools import reduce, partial
from itertools import *
import operator
from collections import abc

# types
ITERABLE = [tuple, list, set, str, dict, abc.Iterable, map, filter]
SEQUENCE = [tuple, list, str, abc.Sequence]
SIZED = ITERABLE[:]+[abc.Sized]
NUMERIC = [int, float] # complex?

def _easter_eggs():
    improve(int, "fractional", lambda self, other: float("{}.{}".format(self, other)))

def _functional_iterables():
    improve(dict, "merge", lambda self, other: {**self, **other})

    for t in SIZED:
        improve(t, "size", lambda self: len(self) if hasattr(self, "__len__") else len(list(self)))
        improve(t, "len", lambda self: len(self) if hasattr(self, "__len__") else len(list(self)))
        improve(t, "length", lambda self: len(self) if hasattr(self, "__len__") else len(list(self)))

    for t in ITERABLE:
        improve(t, "map", lambda self, f: map(f, self))
        improve(t, "filter", lambda self, f: filter(f, self))
        improve(t, "reduce", lambda self, f, inital=None: reduce(f, self, initial))

        improve(t, "any", lambda self, f=None: any(self) if f is None else any(map(f, self)))
        improve(t, "exists", lambda self, f=None: any(self) if f is None else any(map(f, self)))
        improve(t, "all", lambda self, f=None: all(self) if f is None else all(map(f, self)))
        improve(t, "every", lambda self, f=None: all(self) if f is None else all(map(f, self)))

        improve(t, "min", lambda self: min(self))
        improve(t, "max", lambda self: max(self))

        improve(t, "sum", lambda self: reduce(operator.add, self))
        improve(t, "product", lambda self: reduce(operator.mul, self))

    for t in SEQUENCE:
        improve(t, "head", lambda self: self[0])
        improve(t, "first", lambda self: self[0])
        improve(t, "last", lambda self: self[-1])

        improve(t, "init", lambda self: self[:-1])
        improve(t, "tail", lambda self: self[1:])

        improve(t, "drop", lambda self, n: self[n:])
        improve(t, "take", lambda self, n: self[:n])

        improve(t, "dropwhile", lambda self, f: dropwhile(f, self))
        improve(t, "takewhile", lambda self, f: takewhile(f, self))

        improve(t, "cycle", lambda self: cycle(self))
        improve(t, "repeat", lambda self, n=None: repeat(self, None))

        improve(t, "reversed", lambda self: reversed(self))
        improve(t, "sorted", lambda self: sorted(self))

        improve(t, "zip", lambda self, other: zip(self, other))
        improve(t, "unzip", lambda self: zip(*self))
        improve(t, "index_zip", lambda self, other: zip(range(len(self)), self))

def _requests():
    import requests
    class RequestsWrapper(object):
        def __init__(self, url):
            self.url = url
        get = property(lambda self: partial(requests.get, (self.url)))
        post = property(lambda self: partial(requests.post, (self.url)))
        head = property(lambda self: partial(requests.head, (self.url)))
        options = property(lambda self: partial(requests.options, (self.url)))

    improve(str, "request", property(lambda self: RequestsWrapper(self)))
    improve(str, "fetch", property(lambda self: requests.get(self).text))

DEFAULT_FEATURES = [
    "functional_iterables"
]
EXTRA_FEATURES = [
    "easter_eggs",
    "json",
    "requests",
]

class Installer(list):
    """Manages installed features."""
    def install(self, feature):
        if feature not in self:
            try:
                installer = getattr(sys.modules[__name__], "_"+feature)
            except AttributeError:
                raise ValueError("Invalid feature: '{}'".format(feature))
            installer()
            self.append(feature)

installer = Installer()

def install(extras=False):
    features = DEFAULT_FEATURES[:]
    if isinstance(extras, bool):
        if extras:
            features += EXTRA_FEATURES[:]
    elif isinstance(extras, (tuple, list)):
        features += extras[:]
    elif isinstance(extras, str):
        features += [extras]
    else:
        raise ValueError("Extras must be either bool or list")
    for feature in features:
        if feature not in DEFAULT_FEATURES+EXTRA_FEATURES:
            raise ValueError("Unknown feature: '{}'".format(feature))
        installer.install(feature)

if __name__ == "__main__":
    pass
else:
    install()
