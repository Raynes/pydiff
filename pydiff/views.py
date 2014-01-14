from flask import Response, request
from pydiff.diff import difftexts
from pydiff import app
from json import loads, dumps

@app.route('/diff', methods=['POST'])
def post_diff():
    texts = loads(request.get_data(as_text=True))
    diff = difftexts(texts['left'], texts['right'], texts.get('unified'))
    return Response(dumps(diff), mimetype='application/json')
