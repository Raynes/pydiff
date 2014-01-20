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

Here is an example using httpie to connect to the API:

```
$ ls > foo.txt
$ ls world/ > bar.txt
$ http POST localhost:5000/diff left=@foo.txt right=@bar.txt unified=true
HTTP/1.0 200 OK
Content-Length: 326
Content-Type: application/json
Date: Mon, 20 Jan 2014 07:45:52 GMT
Server: Werkzeug/0.9.4 Python/3.3.3

{
    "output": "--- /var/folders/_6/t27l5t253jg8hmkjj214lt140000gp/T/tmp2j1mqr\t2014-01-19 23:45:52.000000000 -0800\n+++ /var/folders/_6/t27l5t253jg8hmkjj214lt140000gp/T/tmppdpjn5\t2014-01-19 23:45:52.000000000 -0800\n@@ -1 +1 @@\n-@foo.txt\n\\ No newline at end of file\n+@bar.txt\n\\ No newline at end of file\n",
    "same": false
}
```
