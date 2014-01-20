"""This module contains the difftexts function that does the
actual diff on the strings.

"""
import difflib


def rundiff(left, right, f):
    """Higher order function for doing the tedious
    work around turning a diff into something useful
    as a response. Takes two strings and a function
    that takes at least two arguments (the strings)
    and returns an iterable that produces strings.

    If the diffing function produces no output, the
    resulting diff will have 'same' set to True.
    Otherwise it'll be false and 'output' will be
    joined output of the diffing function.

    """
    diffed = '\n'.join(f(left.splitlines(), right.splitlines()))
    if diffed:
        return {'same': False, 'output': diffed}
    else:
        return {'same': True}


def difftexts(left, right, kind):
    """Run a unified or context diff on two strings."""
    if kind == 'unified':
        return rundiff(left, right, difflib.unified_diff)
    elif kind == 'context':
        return rundiff(left, right, difflib.context_diff)
    else:
        return {'error': 'Unsupported "kind"'}
