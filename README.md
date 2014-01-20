# Pydiff

Pydiff is a little webservice for diffing strings! It is dead simple. There is
no UI or front-facing interface. It is simply an API with one endpoint.

I have a copy hosted at http://pydiff.raynes.me/.

## Usage

Get dependencies by doing this:

```
pip install -r requirements.txt
```

Next, do the following:

```
python runserver.py
```

You can customize how the server runs by using environment variables:

```
DEBUG=1 PORT=3243 python runserver.py
```

Here are some examples using httpie to connect to the API:

```
$ http POST localhost:5000/diff left=$'foo\nbar\nbaz' right=$'foo\nbaz\nbar'
HTTP/1.0 200 OK
Content-Length: 86
Content-Type: application/json
Date: Mon, 20 Jan 2014 21:31:25 GMT
Server: Werkzeug/0.9.4 Python/3.3.3

{
    "output": "--- \n\n+++ \n\n@@ -1,3 +1,3 @@\n\n foo\n+baz\n bar\n-baz",
    "same": false
}

$ http POST localhost:5000/diff left=$'foo\nbar\nbaz' right=$'foo\nbaz\nbar' kind=context
HTTP/1.0 200 OK
Content-Length: 136
Content-Type: application/json
Date: Mon, 20 Jan 2014 21:32:14 GMT
Server: Werkzeug/0.9.4 Python/3.3.3

{
    "output": "*** \n\n--- \n\n***************\n\n*** 1,3 ****\n\n  foo\n  bar\n- baz\n--- 1,3 ----\n\n  foo\n+ baz\n  bar",
    "same": false
}

$ http POST localhost:5000/diff left=$'foo\nbar\nbaz' right=$'foo\nbar\nbaz' kind=context
HTTP/1.0 200 OK
Content-Length: 14
Content-Type: application/json
Date: Mon, 20 Jan 2014 21:32:53 GMT
Server: Werkzeug/0.9.4 Python/3.3.3

{
    "same": true
}
```
