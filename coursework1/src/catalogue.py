from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root(name='Test'):
    user = name
    return render_template('hello.html', user=user)

@app.route("/artists/")
def artists():
    artists = ['Bugsy Malone', 'Dej Loaf', 'Kano', 'Skepta']
    return render_template('artists.html', artists = artists)

@app.route("/albums/")
def albums():
    return render_template('albums.html')

@app.route("/genres/")
def genres():
    return render_template('genres.html')

@app.route("/tracks/")
def tracks():
    return render_template('tracks.html')

if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
