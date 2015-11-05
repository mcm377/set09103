from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/artists/")
def artists():
    artists = ['Avicii', 'Bugzy Malone', 'Calvin Harris', 'Clean Bandit', 'Drake', 'Eri Kitamura', 'Gorgon City', 'Kano', 'The Killers', 'Nero', 'Rudimental', 'TRF']
    return render_template('artists.html', artists = artists)

@app.route("/artists/<artist>")
def get_artist(artist):
    return render_template('artist_details.html', artist = artist)

@app.route("/albums/")
def albums():
    albums = sorted(['True', 'Walk With Me', 'I Created Disco', 'Ready For The Weekend', '18 Months', 'Motion', 'New Eyes', '2010', 'OriginL ClassC', 'Live fron France', 'Thank Me Later', 'Take Care', 'Nothing Was The Same', 'Re;Story', 'Shomei (証×明)', 'Sirens', 'The Crypt', 'Real', 'Home Sweet Home', 'London Town', '140 Grime Street', 'Method To The Meadness', 'Welcome Reality', 'Between II Worlds', 'Home', 'We The Generation', 'Hot Fuss', 'Sams Town', 'Day & Age', 'Battle Born', 'GRAVITY'])
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
