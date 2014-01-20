import os
from pydiff import app

if __name__ == '__main__':
    port = int(os.environ.get('PORT') or 5000)
    debug = os.environ.get('DEBUG')
    app.run(debug=debug, port=port)
