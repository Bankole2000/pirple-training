from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    print("Someone Visited the Home page")
    return render_template('index.html')


@app.route('/about', methods=['GET'])
def about():
    print("Here's a message")
    return render_template('about.html')


if __name__ == '__main__':
    app.run(port=5000, debug=True)
