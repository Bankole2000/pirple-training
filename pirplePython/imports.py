"""
Name: imports.py V1.0
Auth: Bankole Esan
Desc: Pirple.com Python Homework #10
Task: Importing
"""
import sys
import urllib
from urllib import parse, request
from os import system, name
from time import sleep
from colorama import init, Fore, Back, Style
init()

# Clear Screen function


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


shortTime = 1  # short pauses time length
longTime = 2  # long pauses time length
demoUrl = "https://example.com"  # url for demo sample

# Menu Option 1 functions


def viewNotes():
    clear()
    print(Fore.CYAN + "\n - [1] Notes on the 'urllib' package")
    print("-"*40 + Fore.RESET)
    print(Fore.MAGENTA + "urllib " + Fore.RESET +
          "is a python package that contains several modules \nthat helps with building, loading and parsing URLS. It contains ")
    print("5 main modules - " + Fore.MAGENTA + "request" + Fore.RESET + ", " + Fore.MAGENTA + "response" + Fore.RESET + ", " +
          Fore.MAGENTA + "error" + Fore.RESET + ", " + Fore.MAGENTA + "parse" + Fore.RESET + ", and " + Fore.MAGENTA + "robotparser" + Fore.RESET + ".\n")
    print(" - 1. " + Fore.MAGENTA + "request" + Fore.RESET + " : ", end="")
    print("This module is used to open urls (sending requests)")
    print(" - 2. " + Fore.MAGENTA + "response" + Fore.RESET + " : ", end="")
    print("This module is used internally by the request module to handle requests")
    print(" - 3. " + Fore.MAGENTA + "error" + Fore.RESET + " : ", end="")
    print("This module handles request errors and exceptions")
    print(" - 4. " + Fore.MAGENTA + "parse" + Fore.RESET + " : ", end="")
    print("This module contains several URL parsing functions")
    print(" - 5. " + Fore.MAGENTA + "robotparser" + Fore.RESET + " : ", end="")
    print("This module parses robots.txt files for permissions to bots and crawlers etc")
    input("\nPress Enter to Continue...")
    clear()
    print(Fore.CYAN + "\n - [1] Notes on the 'urllib' package")
    print("-"*40 + Fore.RESET)
    print("To begin using any of the" + Fore.MAGENTA + " urllib " + Fore.RESET +
          "modules, we first import \nthe package (or the modules we wish to use) it into the file or REPL like so:")
    print(Fore.CYAN + ">>> import " + Fore.MAGENTA +
          "urllib" + Fore.RESET, end="")
    print(" # OR ", end="")
    print(Fore.CYAN + "\n>>> from " + Fore.MAGENTA +
          "urllib " + Fore.CYAN + "import " + Fore.MAGENTA +
          "response" + Fore.RESET+", " + Fore.MAGENTA + " parse", end="")
    print(Fore.RESET + "\nThis gives us access to very useful properties \nand methods provided by the package and it's modules. ")
    print("Methods like: ")
    print(" - 1. " + Fore.MAGENTA + "request." + Fore.GREEN +
          "urlopen()" + Fore.RESET + " : ", end="")
    print("Used to open urls (takes in a url string as a parameter)")
    print(" - 2. " + Fore.MAGENTA + "parse." + Fore.GREEN +
          "urlencode()" + Fore.RESET + " : ", end="")
    print("Used to build a query string from a dictionary")
    print(" - 3. " + Fore.MAGENTA + "parse." + Fore.GREEN +
          "urlparse()" + Fore.RESET + " : ", end="")
    print("Returns url details like url path, querystring, scheme, fragments, and netloc")
    print(" - 4. " + Fore.MAGENTA + "parse." + Fore.GREEN +
          "urlsplit()" + Fore.RESET + " : ", end="")
    print("Splits the url into it's individual components like path, scheme, params etc")
    print(" - 5. " + Fore.MAGENTA + "parse." + Fore.GREEN +
          "parse_qsl()" + Fore.RESET + " : ", end="")
    print("Parses a query string into a list of its keys and values")

    input("\nEnd of Notes - Press Enter to Return to the Menu...")

    mainMenu()


# Menu option 3 handler
def demoParser(url):
    clear()
    print(Fore.CYAN + "\n - [3] Testing 'urllib' parse module")
    print("-"*40 + Fore.RESET)
    print("Requested URL => ", url, end="")
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> ", end="")
    print("parsedUrl = " + Fore.MAGENTA + "parse." + Fore.GREEN + "urlparse"
          "(" + Fore.YELLOW + url + Fore.GREEN + ")")
    parsedUrl = parse.urlparse(url)
    sleep(shortTime)
    print(parsedUrl)
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> ", end="")
    print("splitUrl = " + Fore.MAGENTA + "parse." + Fore.GREEN + "urlsplit"
          "(" + Fore.YELLOW + url + Fore.GREEN + ")")
    splitUrl = parse.urlsplit(url)
    sleep(shortTime)
    print(splitUrl)
    if len(parse.urlsplit(url).query) > 0:
        sleep(shortTime)
        print(Fore.CYAN + "\n>>> ", end="")
        print("queryString = " + Fore.MAGENTA + "parse." + Fore.GREEN + "urlsplit"
              "(" + Fore.YELLOW + url + Fore.GREEN + ")." + Fore.RED + "query" + Fore.GREEN)
        queryString = parse.urlsplit(url).query
        sleep(shortTime)
        print(queryString)
        sleep(shortTime)
        print(Fore.CYAN + "\n>>> ", end="")
        print("queryParamsQsl = " + Fore.MAGENTA + "parse." + Fore.GREEN + "parse_qsl"
              "(" + Fore.YELLOW + queryString + Fore.GREEN + ")." + Fore.RED + "query" + Fore.GREEN)
        queryParamsQsl = parse.parse_qsl(queryString)
        sleep(shortTime)
        print(queryParamsQsl)
        sleep(shortTime)
        print(Fore.CYAN + "\n>>> ", end="")
        print("querydict = dict(" + Fore.MAGENTA +
              str(queryParamsQsl) + Fore.CYAN + ")" + Fore.GREEN)
        querydict = dict(queryParamsQsl)
        sleep(shortTime)
        print(querydict)
        sleep(shortTime)
        print("\n", end="")
        print(u'\u2713'*3, end="")
        print(Fore.RESET + " The URL has been completely parsed")

    else:
        print(f"The URL has no query string to parse")
    input("Press Enter to Continue...")
    mainMenu()


# Menu Option 2 handler
def viewCommands():
    clear()
    print(Fore.CYAN + "\n - [2] 'urllib' package code samples")
    print("-"*40 + Fore.RESET)
    print("Here's some code samples showing the usage of \nthe " + Fore.MAGENTA + "urllib " + Fore.RESET +
          "package - specifically the request module.")
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> import " + Fore.MAGENTA +
          "urllib " + Fore.RESET, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# imports the 'urllib' package ", end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> dir(" + Fore.MAGENTA +
          "urllib" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t\t# returns the contents of the package", end="")
    sleep(longTime)
    print("\n\t (Let's run the command...)")
    sleep(longTime)
    print(Fore.GREEN + str(dir(urllib)), end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# notice the 'response' and 'parse' modules ", end="")
    sleep(longTime)
    print(Fore.CYAN + "\n\n>>> from " + Fore.MAGENTA +
          "urllib " + Fore.CYAN + "import " + Fore.MAGENTA +
          "response " + Fore.RESET, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# imports the 'response' module from the 'urllib' package ", end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> ", end="")
    print("resp = " + Fore.MAGENTA + "request." + Fore.GREEN + "urlopen"
          "(" + Fore.YELLOW + demoUrl + Fore.GREEN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# sends a 'GET' request to the url", end="")
    sleep(longTime)
    print("\n # And stores the response in the 'resp' variable. ", end="")
    resp = request.urlopen(demoUrl)
    sleep(longTime)
    print(Fore.CYAN + "\n>>> type(" + Fore.YELLOW +
          "resp" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t\t# Let's check the data type of the response", end="")
    sleep(longTime)
    print("\n" + Fore.GREEN, end="")
    print(type(resp), end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# Notice it is a http Response object", end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> dir(" + Fore.YELLOW +
          "resp" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# Returns the properties and methods of the Reponse object", end="")
    sleep(longTime)
    print("\n\t (Let's run the command...)" + Fore.GREEN)
    sleep(longTime)
    print(dir(resp), end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# With these properties and methods we can analyze the Reponse object", end="")

    sleep(longTime)
    print(Fore.CYAN + "\n\n>>> resp." +
          Fore.MAGENTA + "code" + Fore.RESET, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t\t# returns the status code of the response" +
          Fore.GREEN, end="")
    sleep(longTime)
    print("\n", end="")
    print(resp.code, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# 200 = OK, 403 = Forbidden, 404 = Not Found, 500 = Server Error", end="")

    sleep(longTime)
    print(Fore.CYAN + "\n>>> resp." +
          Fore.MAGENTA + "_method" + Fore.RESET, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# returns the request method used" +
          Fore.GREEN, end="")
    sleep(longTime)
    print("\n", end="")
    print(resp._method, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# This was a 'GET' request. 'POST', 'PUT' and 'HEAD' requests etc are also possible.", end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> resp." + Fore.MAGENTA +
          "length" + Fore.RESET, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t\t# returns the size of the response in bytes" +
          Fore.GREEN, end="")
    sleep(longTime)
    print("\n", end="")
    print(resp.length, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# Size of the response object in bytes", end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> resp." + Fore.MAGENTA +
          "peek()" + Fore.RESET, end="")
    sleep(shortTime)
    print(Fore.RESET + "\t\t# returns the bytes object of the response html", end="")
    sleep(longTime)
    print("\n\t (Let's run the command...)" + Fore.GREEN)
    sleep(longTime)
    print(resp.peek(), end="")
    sleep(longTime)
    print(Fore.RESET + "\n# The 'b' prefix means it's a bytes datatype" +
          Fore.GREEN, end="")
    sleep(longTime)
    print(Fore.CYAN + "\n\n>>> data = " + Fore.MAGENTA +
          "resp." + Fore.YELLOW + "read()", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# method to retrieve the body of the response in the variable 'data'" + Fore.GREEN, end="")
    sleep(longTime)
    data = resp.read()
    print(Fore.CYAN + "\n>>> type(" + Fore.YELLOW +
          "data" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# returns the datatype of the response content" +
          Fore.GREEN, end="")
    sleep(longTime)
    print("\n", end="")
    print(type(data), end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# We see it's of type bytes" + Fore.GREEN, end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> len(" + Fore.YELLOW +
          "data" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# returns the size of the data " + Fore.GREEN, end="")
    sleep(longTime)
    print("\n", end="")
    print(len(data), end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# We see the size in bytes" + Fore.GREEN, end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> html = " + Fore.MAGENTA +
          "data." + Fore.GREEN + "decode(" + Fore.YELLOW + "\"UTF-8\" " + Fore.GREEN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# The data is in utf-8 format so we decode it to retrieve the html" +
          Fore.GREEN, end="")
    html = data.decode("UTF-8")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> type(" + Fore.YELLOW +
          "html" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# returns the datatype of the now decoded html content" + Fore.GREEN, end="")
    sleep(longTime)
    print("\n", end="")
    print(type(html), end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# We see it's of type String" + Fore.GREEN, end="")
    sleep(longTime)
    print(Fore.CYAN + "\n>>> print(" + Fore.YELLOW +
          "html" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print(Fore.RESET + "\t# This will Print out the web page we've fetched " +
          Fore.RESET, end="")
    sleep(longTime)
    print("\n\t (Let's run the command...)\n" + Fore.GREEN)
    sleep(longTime)
    print(html)
    if resp.code == 200:
        print(u'\u2713'*3, end="")
        print(Fore.RESET + " SUCCESS!!! We retrieved the webpage using the" +
              Fore.MAGENTA + " urllib." + Fore.CYAN + "request " + Fore.RESET + "module!")
    else:
        print(Fore.RESET + u'\u274C', end="")
        print(Fore.RESET + " uh oh!  The" +
              Fore.MAGENTA + "urllib." + Fore.CYAN + "request " + Fore.RESET + "module works, but we got an error code ", str(resp.code))
        print("Maybe Try a different URL")

    input("\nPress Enter to continue...")
    mainMenu()


# Menu option 3 part 1
def runCode(url):
    clear()
    print(Fore.CYAN + "\n - [3] Testing 'urllib' request module")
    print("-"*40 + Fore.RESET)
    print("Requested URL => ", url, end="")
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> ", end="")
    print("resp = " + Fore.MAGENTA + "request." + Fore.GREEN + "urlopen"
          "(" + Fore.YELLOW + url + Fore.GREEN + ")", end="")
    resp = request.urlopen(url)
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> type(" + Fore.YELLOW +
          "resp" + Fore.CYAN + ")", end="")
    sleep(shortTime)
    print("\n" + Fore.GREEN, end="")
    print(type(resp), end="")
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> dir(" + Fore.YELLOW +
          "resp" + Fore.CYAN + ")" + Fore.GREEN, end="")
    sleep(shortTime)
    print(dir(resp), end="")
    sleep(shortTime)
    print(Fore.CYAN + "\n\n>>> resp." +
          Fore.MAGENTA + "_method" + Fore.RESET, end="")
    print(Fore.CYAN + ", resp." +
          Fore.MAGENTA + "code" + Fore.RESET, end="")
    sleep(shortTime)
    print("\n" + Fore.GREEN, end="")
    print(resp._method, end=", ")
    print(resp.code, end="")
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> resp." + Fore.MAGENTA +
          "length" + Fore.RESET, end="")
    sleep(shortTime)
    print("\n" + Fore.GREEN, end="")
    print(resp.length, end="")
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> data = " + Fore.MAGENTA +
          "resp." + Fore.YELLOW + "read()", end="")
    sleep(shortTime)
    data = resp.read()
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> html = " + Fore.MAGENTA +
          "data." + Fore.GREEN + "decode(" + Fore.YELLOW + "\"UTF-8\" " + Fore.GREEN + ")", end="")
    html = data.decode("UTF-8")
    sleep(shortTime)
    print(Fore.CYAN + "\n>>> print(" + Fore.YELLOW +
          "html" + Fore.CYAN + ")" + Fore.GREEN)
    sleep(shortTime)
    print(html)
    if resp.code == 200:
        print(u'\u2713'*3, end="")
        print(Fore.RESET + " SUCCESS!!! We retrieved the webpage using the" +
              Fore.MAGENTA + " urllib." + Fore.CYAN + "request " + Fore.RESET + "module!")
    else:
        print(Fore.RESET + u'\u274C', end="")
        print(Fore.RESET + " uh oh!  The" +
              Fore.MAGENTA + "urllib." + Fore.CYAN + "request " + Fore.RESET + "module works, but we got an error code ", str(resp.code))
        print("Maybe Try a different URL")

    input("\nPress Enter to continue...")
    demoParser(url)


# Main menu
def mainMenu():
    clear()
    print(Fore.GREEN + "\n====*** Intro to the " + Fore.MAGENTA +
          " URLLIB " + Fore.GREEN + " package ***====" + Style.RESET_ALL)
    print("Learn about the URLLIB python package ")
    print(Fore.CYAN + " [1]" + Fore.RESET +
          " View Notes on the URLLIB package")
    print(Fore.CYAN + " [2]" + Fore.RESET +
          " View Sample URLLIB code and commands")
    print(Fore.CYAN + " [3]" + Fore.RESET + " Try out the URLLIB")
    print(Fore.CYAN + " [4]" + Fore.RESET + " Exit Program")

    while True:
        print("\n - Please select an option " + Fore.CYAN +
              "(1 - 4)" + Fore.RESET+": ", end="")
        option = input()
        if int(option) == 1:
            viewNotes()
        elif int(option) == 2:
            viewCommands()
        elif int(option) == 3:
            newUrl = input("Please enter a URL : ")
            runCode(newUrl)
        elif int(option) == 4:
            sys.exit(0)


mainMenu()
