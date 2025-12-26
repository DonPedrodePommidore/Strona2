from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def home():
    db = sqlite3.connect('movies.db')
    cursor = db.cursor()
    if request.method == 'POST':
        movies_to_remove_ids = request.form.getlist('movieToRemove')
        for id in movies_to_remove_ids:
            cursor.execute('DELETE FROM movies WHERE rowid = ?', (id,))
        db.commit()
    cursor.execute('SELECT rowid, * FROM movies')
    return render_template('home.html', movies=cursor)
@app.route('/addMovie', methods=['GET', 'POST'])
def add_movie():
    if request.method == 'POST':
        movieTitle = request.form.get('title')
        movieYear= request.form.get('year')
        movieActors= request.form.get('actors')
        if not movieTitle:
            return "Wprowadź nazwę filmu"
        #dodać do bazy
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