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
    return "Hello Napier!!! :D"

@app.route("/genres/")
def genres():
    return "Goodbye cruel world :("

@app.route("/tracks/")
def tracks():
    return "Hello Napier!!! :D"

if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
