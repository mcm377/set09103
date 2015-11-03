from flask import Flask
app = Flask(__name__)

@app.route("/")
def root():
    return "The default, 'root' route"

@app.route("/artists/")
def artists():
    return "Hello Napier!!! :D"

@app.route("/albums/")
def albums():
    return "Hello Napier!!! :D"

@app.route("/genres/")
def genres():
    return "Goodbye cruel world :("

@app.route("/tracks/")
def artists():
    return "Hello Napier!!! :D"

if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
