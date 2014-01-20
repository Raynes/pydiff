"""This module contains the difftexts function that does the
actual diff on the strings.

"""
import os
import tempfile
from sh import diff


def difftexts(left, right, unified):
    """Run diff on two temporary files filled with left and right
    respectively. If the files are both the same, returns a dict
    with key 'same' bound to True. Otherwise 'same' is bound to
    False and 'output' is bound to the output of the diff command

    """
    leftf, leftfs = tempfile.mkstemp()
    rightf, rightfs = tempfile.mkstemp()
    try:
        os.write(leftf, left.encode('utf-8'))
        os.write(rightf, right.encode('utf-8'))
        diffed = ''
        if unified == 'true':
            diffed = diff("-u", leftfs, rightfs, _ok_code=[0, 1, 2]).stdout
        else:
            diffed = diff(leftfs, rightfs, _ok_code=[0, 1, 2]).stdout
        output = diffed.decode('utf-8')
        if diffed:
            return {'same': False,
                    'output': output}
        else:
            return {'same': True}
    finally:
        os.close(leftf)
        os.close(rightf)
        os.remove(leftfs)
        os.remove(rightfs)
