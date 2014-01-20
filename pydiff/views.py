"""This service has a very simple API and thus the views
can be reasonably collapsed into this file.

"""
import json
import flask
from pydiff import app
import pydiff.diff as diff


@app.route('/diff', methods=['POST'])
def post_diff():
    """A POST endpoint that takes a 'left' string and a
    'right' string and performs a diff on it. if 'kind'
    is passed, the type of diff performed is determined
    by its value. Possible values are 'context' and
    'unified', and the default is 'unified'

    """
    texts = json.loads(flask.request.get_data(as_text=True))
    left = texts['left']
    right = texts['right']
    kind = texts.get('kind') or 'unified'
    result = diff.difftexts(left, right, kind)
    if result.get('error'):
        status = 422
    else:
        status = 200
    return flask.Response(
        json.dumps(result),
        mimetype='application/json',
        status=status
    )


@app.route('/', methods=['GET'])
def get_help():
    """A GET endpoint that simply redirects to the
    Github README for pydiff.

    """
    url = 'https://github.com/Raynes/pydiff/blob/master/README.md'
    return flask.redirect(url)
