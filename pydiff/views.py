import json
import flask
from pydiff import app
import pydiff.diff as diff


@app.route('/diff', methods=['POST'])
def post_diff():
    texts = json.loads(flask.request.get_data(as_text=True))
    left = texts['left']
    right = texts['right']
    result = diff.difftexts(left, right, texts.get('unified'))
    return flask.Response(json.dumps(result), mimetype='application/json')
