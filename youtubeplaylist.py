from flask import Flask
from flask import render_template, make_response, request, flash
from youtube import createPlaylist

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

@app.route('/playlistpage', methods=['GET', 'POST'])
def playlistpage():
    playlistname = request.args.get('playlistname')
    artists = []
    for i in range(5):
        arg = "artist"
        arg += str(i + 1)
        artist = request.args.get(arg)

        if artist is not None:
            artists.append(artist)



   
    html = render_template('playlistpage.html')
    response = make_response(html)
    return response

if __name__ == '__main__':
    app.run(debug=True)