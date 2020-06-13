"""
Name: imports.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #10
Task: Importing
"""
# # Using python to send Get requests and parse response

# # URL => Uniform Resource Locator
# # Protocol: http, https, ftp, smtp etc...
# # Host : en.wikipedia.org
# # Port : http = 80, https = 443
# # Path: wiki/URL
# # Query string (keyvalue pairs): key=value&life=42
# # Fragment: History

# # urllib is a package that helps to build load and parse urls
# # Contains 5 modules =>
# # 1. request: open urls
# # 2. response: used internally by the request module
# # 3. error: handles request exceptions
# # 4. parse: useful URL functions
# # 5. robotparser: parses robots.txt files for permissions to bots and crawlers etc

from urllib import parse
from urllib import request
import urllib
# print(dir(urllib))

# print(dir(request))
# # Files: open(file)
# # URLS: urlopen(url)

# resp = request.urlopen("https://www.wikipedia.org")
# print(type(resp))
# print(dir(resp))
# print(resp.code)  # returns response code
# print(resp.length)  # returns size in bytes
# print(resp.peek())  # returns bytes object of html
# data = resp.read()
# print(type(data))
# print(len(data))
# # The data is in utf-8 format so to decode we can do
# html = data.decode("UTF-8")
# print(type(html))
# print(html)

# print(resp.read())  # nothin happens when we try to read the response a second time
# # This is because python closes the connection once the response is read

# # Exampe 2:
# # Will return a 403 error
# resp = request.urlopen("https://www.google.com/search?q=socratica")
# # response codes => 200: okay, 400; Bad request, 403: forbidden, 404: not found

# # https://www.youtube.com/watch?v=EuC-yVzHhMI&t=5m56s

# Building a query string
qs = "v="+"EuC-yVzHhMI"+"&"+"t="+"5m56s"
# but there is a better way by using the parse module

print(dir(parse))
# we will use the 'urlencode' function of the parse module
# first create a dictionary of the query params
params = {"v": "EuC-yVzHhMI", "t": "5m56s"}
# then use the urlencode fxn
newUrl = "https://www.youtube.com/watch?v=QTklKBndYgg&list=PLxl69kCRkiI2AY9DlxbIbrqkFo-0Rm6nE"
parsed = parse.urlparse(newUrl)
splitUrl = parse.urlsplit(newUrl)
queryparamsqsl = parse.parse_qsl(parse.urlsplit(newUrl).query)
querystring = parse.urlencode(params)
print(querystring)
print(parsed, type(parsed))
# print(parse.splitvalue(parsed.query))
print(splitUrl, dict(queryparamsqsl))
# we can now build the URL
# url = "https://www.youtube.com/watch" + "?" + querystring

# resp = request.urlopen(url)
# print(resp.isclosed())
# print(resp.code)
# html = resp.read().decode("utf-8")
# print(html[:500])  # returns the first 500 characters of the html


# Interacting with API
