from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    cursor.execute('SELECT * FROM movies')
    return render_template('home.html', movies=cursor)
@app.route('/addMovie', methods=['GET', 'POST'])
def add_movie():  # put application's code here
    if request.method == 'POST':
        movieTitle = request.form.get('title')
        movieYear= request.form.get('year')
        movieActors= request.form.get('actors')
        #dodać do bazy
        #cursor.execute(query='INSERT INTO movies (title, year, actors) VALUES ("{title}",{year},"{actors}")',)
        db = sqlite3.connect('movies.db')
        cursor = db.cursor()
        cursor.execute('INSERT INTO movies (title, year, actors) VALUES (?, ?, ?)', (movieTitle, movieYear, movieActors))
        db.commit()
        return redirect(url_for('home'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run()
#przy usuwaniu potrzebujemy opakowac liste w formularz
#kazdemu checkboxowi trzeba podac ID