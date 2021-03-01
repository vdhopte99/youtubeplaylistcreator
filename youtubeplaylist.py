from flask import Flask
from flask import render_template, make_response, request, flash

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET'])
def home():
    html = render_template('homepage.html')
    response = make_response(html)
    return response

@app.route('/enterartists', methods=['GET'])
def enterartists():
    html = render_template('enterartists.html')
    response = make_response(html)
    return response

if __name__ == '__main__':
    app.run(debug=True)