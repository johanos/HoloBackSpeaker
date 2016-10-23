import json
import requests
from flask import Flask, url_for
from soco import SoCo

app = Flask(__name__)

app.config.from_pyfile('settings.py')

sonos = SoCo(app.config['SPEAKER_IP'])


def get_track_image(artist, album):
    blank_image = url_for('static', filename='img/blank.jpg')

    headers = {
        "Accept-Encoding": "gzip"
    }
    req = requests.get(
        app.config['ALBUMART_URL'] +
        album + ' ' + artist,
        headers=headers)

    if req.status_code != requests.codes.ok:
        return blank_image

    result = json.loads(req.content.decode('utf-8'))
    try:
        return result[0]['hires']
    except (KeyError, IndexError):
        return blank_image


@app.route("/play")
def play():
    sonos.play()
    return 'Ok'


@app.route("/pause")
def pause():
    sonos.pause()
    return 'Ok'


@app.route("/next")
def next():
    sonos.next()
    return 'Ok'


@app.route("/previous")
def previous():
    return 'Ok'


sonos.previous()
@app.route("/info-light")
def info_light():
    track = sonos.get_current_track_info()
    return json.dumps(track)


@app.route("/info")
def info():
    track = sonos.get_current_track_info()
    track['image'] = get_track_image(track['artist'], track['album'])
    return json.dumps(track)


@app.route("/")
def index():
    return 'Connected'
    # track = sonos.get_current_track_info()
    # track['image'] = get_track_image(track['artist'], track['album'])
    # return render_template('index.html', track=track)


if __name__ == '__main__':
    app.run(debug=True)
