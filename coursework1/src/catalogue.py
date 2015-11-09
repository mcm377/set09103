# coding: utf-8
from flask import Flask, render_template

app = Flask(__name__)

artist_albums = {'Avicii': ['True'], 'Bugzy Malone': ['Walk With Me'], 'Calvin Harris': ['I Created Disco', 'Ready For The Weekend', '18 Months', 'Motion'], 'Clean Bandit': ['New Eyes', '2010', 'OriginL ClassC', 'Live fron France'], 'Drake': ['Thank Me Later', 'Take Care', 'Nothing Was The Same'], 'Eri Kitamura': ['Re;Story', u'Shomei (証×明)'], 'Gorgon City': ['Sirens'], 'Kano': ['Home Sweet Home', 'London Town', '140 Grime St', 'Method To The Meadness'], 'The Killers': ['Hot Fuss', 'Sam\'s Town', 'Day & Age'], 'Nero': ['Welcome Reality', 'Between II Worlds'], 'Rudimental': ['Home', 'We The Generation'], 'TRF': ['GRAVITY']}

artist_tracks = {'Avicii': ['Wake Me Up', 'You Make Me', 'Hey Brother', 'Addicted To You', 'Dear Boy', 'Liar Liar', 'Shame on Me', 'Lay Me Down' , 'Hope There\'s Someone', 'Heart Upon My Sleeve'], 'Bugzy Malone': ['Ready to Blow', 'Watch Your Mouth', 'M.E.N', 'Get Gassed', 'Pain', 'Get Paid', 'Pagans', 'Walk With Me'], 'Calvin Harris': ['Acceptable in the 80s', 'The Girls', 'I\'m Not Alone', 'Ready for the Weekend', 'Bounce', 'Feels So Close', 'Summer', 'Outside'], 'Clean Bandit': ['A+E', 'Mozart\'s House', 'Dust Clears', 'Rather Be', 'Extraordinary', 'Come Over', 'Real Love', 'Stronger'], 'Drake': ['Forever', 'Over', 'Miss Me', 'Headlines', 'Make Me Proud', 'The Motto', 'Take Care', 'HYFR', 'Started From The Bottom', 'Hold On, We\'re Going Home', 'Worst Behavior'], 'Eri Kitamura': ['Be Starters!', u'Shirushi (紋; Crest)', 'Happy Girl', 'Destiny', 'Miracle Gliders', 'Birth'], 'Gorgon City': ['Real', 'Imagination', 'Ready For Your Love', 'Here For You', 'Unmissable', 'Go All Night'], 'Kano': ['Ps and Qs', 'Typical Me', 'Remember Me', 'Buss It Up', 'This Is The Girl', 'Hustler'], 'The Killers': ['Mr. Brightside', 'Somebody Told Me', 'Smile Like You Mean It', 'When You Were Young', 'Read My Mind', 'Human'], 'Nero': ['Innocence', 'Me & You', 'Guilt', 'Promises', 'Crush On You', 'Satisfy', 'Two Minds'] , 'Rudimental': ['Feel The Love', 'Waiting All Night', 'Right Here', 'Free', 'Powerless', 'Bloodstream', 'Lay It All On Me'], 'TRF': ['lights and any more', 'iNNOVATION', 'do you wanna dance?', 'virtual sea', 'Charge My Life', 'Broken Flower']}

artist_genres = {'Avicii': ['EDM', 'House', 'Progressive House'], 'Bugzy Malone': ['Grime'], 'Calvin Harris': ['EDM'], 'Clean Bandit': ['Electronic'], 'Drake': ['Hip Hop', 'R&B'], 'Eri Kitamura': ['J-pop', 'J-rock', 'Symphonic Rock', 'Symphonic Metal', 'Pop Rock'], 'Gorgon City': ['House', 'Electronic', 'UK Garage'], 'Kano': ['Grime', 'British Hip Hop'], 'The Killers': ['Alternative Rock', 'Indie Rock', 'Post-Punk Revival', 'New Wave', 'Heartland Rock'], 'Nero': ['Dubstep', 'Drum and Bass', 'Electro House', 'Electronic Rock', 'Rave'], 'Rudimental': ['Drum and Bass', 'Liquid Funk', 'Jungle', 'Breakbeat', 'Soul'], 'TRF': ['J-pop', 'J-rock']}

album_tracks = {'True': ['Wake Me Up', 'You Make Me', 'Hey Brother', 'Addicted To You', 'Dear Boy', 'Liar Liar', 'Shame on Me', 'Lay Me Down' , 'Hope There\'s Someone', 'Heart Upon My Sleeve'], 'Walk With Me': ['Ready to Blow', 'Watch Your Mouth', 'M.E.N', 'Get Gassed', 'Pain', 'Get Paid', 'Pagans', 'Walk With Me'], 'I Created Disco': ['Acceptable in the 80s', 'The Girls'], 'Ready For The Weekend': ['I\'m Not Alone', 'Ready for the Weekend'], '18 Months': ['Bounce', 'Feels So Close'], 'Motion': ['Summer', 'Outside'], 'New Eyes': ['A+E', 'Mozart\'s House', 'Dust Clears', 'Rather Be', 'Extraordinary', 'Come Over', 'Real Love', 'Stronger'], 'Thank Me Later': ['Over', 'Miss Me'], 'Take Care': ['Headlines', 'Make Me Proud', 'Take Care', 'HYFR'], 'Nothing Was The Same': ['Started From The Bottom', 'Hold On, We\'re Going Home', 'Worst Behavior'], 'Re;Story': ['Be Starters!', u'Shirushi (紋; Crest)', 'Happy Girl'], u'Shomei (証×明; Proof)': ['Destiny', 'Miracle Gliders', 'Birth'], 'Sirens': ['Real', 'Imagination', 'Ready For Your Love', 'Here For You', 'Unmissable', 'Go All Night'], 'Home Sweet Home': ['Ps and Qs', 'Typical Me', 'Remember Me'], 'London Town': ['Buss It Up', 'This Is The Girl'], '140 Grime St': ['Hustler'], 'Welcome Reality': ['Innocence', 'Me & You', 'Guilt', 'Promises', 'Crush On You'], 'Between II Worlds': ['Satisfy', 'Two Minds'], 'Home': ['Feel The Love', 'Waiting All Night', 'Right Here', 'Free', 'Powerless'], 'We The Generation': ['Bloodstream', 'Lay It All On Me'], 'Hot Fuss': ['Mr. Brightside', 'Somebody Told Me', 'Smile Like You Mean It'], 'Sams Town': ['When You Were Young', 'Read My Mind'], 'Day & Age': ['Human'], 'GRAVITY': ['lights and any more', 'iNNOVATION', 'do you wanna dance?', 'virtual sea', 'Charge My Life', 'Broken Flower']}

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
    for artist in artist_albums.keys():
        if album in artist_albums[artist]:
            album_artist = artist
    return render_template('album_details.html', album = album, album_artist = album_artist, album_genres = artist_genres[album_artist])

@app.route("/genres/")
def genres():
    genres = sorted(['EDM', 'House', 'Progressive House', 'Grime', 'Electronic', 'Hip Hop', 'R&B', 'J-pop', 'J-rock', 'Symphonic Rock', 'Symphonic Metal', 'Pop Rock', 'UK Garage', 'British Hip Hop', 'Alternative Rock', 'Indie Rock', 'Post-Punk Revival', 'New Wave', 'Heartland Rock', 'Dubstep', 'Drum and Bass', 'Electro House', 'Electronic Rock', 'Rave', 'Liquid Funk', 'Jungle', 'Breakbeat', 'Soul'])
    return render_template('genres.html', genres = genres)

@app.route("/genres/<genre>")
def get_genre(genre):
    genre_artists = []
    genre_tracks = []
    genre_albums = []
    for artist in artist_genres.keys():
        if genre in artist_genres[artist]:
            genre_artists.append(artist)
            for album in artist_albums[artist]:
                genre_albums.append(album)
            for track in artist_tracks[artist]:
                genre_tracks.append(track)
    return render_template('genre_details.html', genre = genre, genre_artists = genre_artists, genre_tracks = genre_tracks, genre_albums = genre_albums)

@app.route("/tracks/")
def tracks():
    tracks = sorted(['Wake Me Up', 'You Make Me', 'Hey Brother', 'Addicted To You', 'Dear Boy', 'Liar Liar', 'Shame on Me', 'Lay Me Down' , 'Hope There\'s Someone', 'Heart Upon My Sleeve', 'Ready to Blow', 'Watch Your Mouth', 'M.E.N', 'Get Gassed', 'Pain', 'Get Paid', 'Pagans', 'Walk With Me', 'Acceptable in the 80s', 'The Girls', 'I\'m Not Alone', 'Ready for the Weekend', 'Bounce', 'Feels So Close', 'Summer', 'Outside', 'A+E', 'Mozart\'s House', 'Dust Clears', 'Rather Be', 'Extraordinary', 'Come Over', 'Real Love', 'Stronger', 'Forever', 'Over', 'Miss Me', 'Headlines', 'Make Me Proud', 'The Motto', 'Take Care', 'HYFR', 'Started From The Bottom', 'Hold On, We\'re Going Home', 'Worst Behavior', 'Be Starters!', u'Shirushi (紋; Crest)', 'Happy Girl', 'Destiny', 'Miracle Gliders', 'Birth', 'Real', 'Imagination', 'Ready For Your Love', 'Here For You', 'Unmissable', 'Go All Night', 'Ps and Qs', 'Typical Me', 'Remember Me', 'Buss It Up', 'This Is The Girl', 'Hustler', 'Mr. Brightside', 'Somebody Told Me', 'Smile Like You Mean It', 'When You Were Young', 'Read My Mind', 'Human', 'Innocence', 'Me & You', 'Guilt', 'Promises', 'Crush On You', 'Satisfy', 'Two Minds', 'Feel The Love', 'Waiting All Night', 'Right Here', 'Free', 'Powerless', 'Bloodstream', 'Lay It All On Me', 'lights and any more', 'iNNOVATION', 'do you wanna dance?', 'virtual sea', 'Charge My Life', 'Broken Flower'])
    return render_template('tracks.html', tracks = tracks)

@app.route("/tracks/<track>")
def get_track(track):
    for artist in artist_tracks.keys():
        if track in artist_tracks[artist]:
            track_artist = artist
    for album in album_tracks.keys():
        if track in album_tracks[artist]:
            track_album = album
    return render_template('track_details.html', track =  track, track_artist = track_artist, track_album = track_album, track_genres = artist_genres[track_artist])

if __name__ == "__main__": 
    app.run(host='0.0.0.0', debug=True)
