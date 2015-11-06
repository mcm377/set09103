# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

artist_albums = {'Avicii': ['True'], 'Bugzy Malone': ['Walk With Me'], 'Calvin Harris': ['I Created Disco', 'Ready For The Weekend', '18 Months', 'Motion'], 'Clean Bandit': ['New Eyes', '2010', 'OriginL ClassC', 'Live fron France'], 'Drake': ['Thank Me Later', 'Take Care', 'Nothing Was The Same'], 'Eri Kitamura': ['Re;Story', u'Shomei (証×明)'], 'Gorgon City': ['Sirens', 'The Crypt', 'Real'], 'Kano': ['Home Sweet Home', 'London Town', '140 Grime Street', 'Method To The Meadness'], 'The Killers': ['Hot Fuss', 'Sam\'s Town', 'Day & Age', 'Battle Born'], 'Nero': ['Welcome Reality', 'Between II Worlds'], 'Rudimental': ['Home', 'We The Generation'], 'TRF': ['GRAVITY']}

artist_tracks = {'Avicii': ['Wake Me Up', 'You Make Me', 'Hey Brother', 'Addicted To You', 'Dear Boy', 'Liar Liar', 'Shame on Me', 'Lay Me Down' , 'Hope There\'s Someone', 'Heart Upon My Sleeve'], 'Bugzy Malone': ['Relegation Riddim', 'Ready to Blow', 'Watch Your Mouth', 'M.E.N', 'Get Gassed', 'Pain', 'Get Paid', 'Pagans', 'Walk With Me'], 'Calvin Harris': ['Acceptable in the 80s', 'The Girls', 'I\'m Not Alone', 'Ready for the Weekend', 'Bounce', 'Feels So Close', 'Summer', 'Outside'], 'Clean Bandit': ['A+E', 'Mozart\'s House', 'Dust Clears', 'Rather Be', 'Extraordinary', 'Come Over', 'Real Love', 'Stronger', 'Disconnect'], 'Drake': ['Forever', 'Over', 'Headlines', 'Make Me Proud', 'The Motto', 'Take Care', 'HYFR', 'Started From The Bottom', 'Hold On, We\'re Going Home', 'Worst Behavior', 'Hotline Bling'], 'Eri Kitamura': ['Before the Moment', 'Tsuyogari', 'Realize', 'Guilty Future', 'Be Starters!', 'Shirushi', 'Happy Girl', 'Destiny', 'Miracle Gliders', 'Birth', u'Tenohira -Show- (掌-show-)', u'Rinrei (凛麗)'], 'Gorgon City': ['Real', 'Intentions', 'Ready For Your Love', 'Here For You', 'Unmissable', 'Go All Night', 'Imagination', 'Saving My Life', 'The Crypt', 'Lover Like You'], 'Kano': ['Ps and Qs', 'Typical Me', 'Remember Me', 'Buss It Up', 'This Is The Girl', 'Hustler', 'Rock n Roller', 'Get Wild', 'Hail'], 'The Killers': ['Mr. Brightside', 'Somebody Told Me', 'Smile Like You Mean It', 'When You Were Young', 'Read My Mind', 'Human'], 'Nero': ['Act Like You Know', 'Innocence', 'Me & You', 'Guilt', 'Promises', 'Crush On You', 'Satisfy', 'Two Minds'] , 'Rudimental': ['Feel The Love', 'Waiting All Night', 'Right Here', 'Free', 'Powerless', 'Bloodstream', 'Lay It All On Me'], 'TRF': ['lights and any more', 'iNNOVATION', 'do you wanna dance?', 'virtual sea', 'Charge My Life', 'Broken Flower']}

artist_genres = {'Avicii': ['EDM', 'House', 'Progressive House'], 'Bugzy Malone': ['Grime'], 'Calvin Harris': ['EDM'], 'Clean Bandit': ['Electronic'], 'Drake': ['Hip Hop', 'R&B'], 'Eri Kitamura': ['J-rock', 'Symphonic Rock', 'Symphonic Metal', 'Pop Rock'], 'Gorgon City': ['House', 'Electronic', 'UK Garage'], 'Kano': ['Grime', 'British Hip Hop'], 'The Killers': ['Alternative Rock', 'Indie Rock', 'Post-Punk Revival', 'New Wave', 'Heartland Rock'], 'Nero': ['Dubstep', 'Drum and Bass', 'Electro House', 'Electronic Rock', 'Rave'], 'Rudimental': ['Drum and Bass', 'Liquid Funk', 'Jungle', 'Breakbeat', 'Soul'], 'TRF': ['J-pop', 'J-rock']}

@app.route("/")
def root():
    return render_template('index.html')

@app.route("/artists/")
def artists():
    artists = ['Avicii', 'Bugzy Malone', 'Calvin Harris', 'Clean Bandit', 'Drake', 'Eri Kitamura', 'Gorgon City', 'Kano', 'The Killers', 'Nero', 'Rudimental', 'TRF']
    return render_template('artists.html', artists = artists)

@app.route("/artists/<artist>")
def get_artist(artist):
    return render_template('artist_details.html', artist = artist, artist_albums = artist_albums[artist], artist_tracks = artist_tracks[artist], artist_genres = artist_genres[artist])

@app.route("/albums/")
def albums():
    albums = sorted(['True', 'Walk With Me', 'I Created Disco', 'Ready For The Weekend', '18 Months', 'Motion', 'New Eyes', '2010', 'OriginL ClassC', 'Live fron France', 'Thank Me Later', 'Take Care', 'Nothing Was The Same', 'Re;Story', u'Shomei (証×明)', 'Sirens', 'The Crypt', 'Real', 'Home Sweet Home', 'London Town', '140 Grime Street', 'Method To The Meadness', 'Welcome Reality', 'Between II Worlds', 'Home', 'We The Generation', 'Hot Fuss', 'Sams Town', 'Day & Age', 'Battle Born', 'GRAVITY'])
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
