# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)
albums = {'Avicii': ['True'], 'Bugzy Malone': ['Walk With Me'], 'Calvin Harris': ['I Created Disco', 'Ready For The Weekend', '18 Months', 'Motion'], 'Clean Bandit': ['New Eyes', '2010', 'OriginL ClassC', 'Live fron France'], 'Drake': ['Thank Me Later', 'Take Care', 'Nothing Was The Same'], 'Eri Kitamura': ['Re;Story', u'Shomei (証×明)'], 'Gorgon City': ['Sirens', 'The Crypt', 'Real'], 'Kano': ['Home Sweet Home', 'London Town', '140 Grime Street', 'Method To The Meadness'], 'The Killers': ['Hot Fuss', 'Sams Town', 'Day & Age', 'Battle Born'], 'Nero': ['Welcome Reality', 'Between II Worlds'], 'Rudimental': ['Home', 'We The Generation'], 'TRF': ['GRAVITY']}

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/artists/")
def artists():
    artists = albums
    return render_template('artists.html', artists = artists)

@app.route("/artists/<artist>")
def get_artist(artist):
    return render_template('artist_details.html', artist = artist)

@app.route("/albums/")
def albums():
    return render_template('albums.html', albums = albums)

@app.route("/albums/<album>")
def get_album(album):
    return render_template('album_details.html', album = album)

@app.route("/genres/")
def genres():
    return render_template('genres.html')

@app.route("/tracks/")
def tracks():
    return render_template('tracks.html')

if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
