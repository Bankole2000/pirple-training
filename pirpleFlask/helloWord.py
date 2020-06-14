from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return makeHtml('<h1>HelloWorld</h1>')


def makeHtml(content):
    return (f'<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Pirple Flask</title></head><body>{content}</body></html>')


@app.route('/about', methods=[GET])

if __name__ == '__main__':
    app.run(port=7000, debug=True)
