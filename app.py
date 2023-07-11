from flask import Flask, render_template, request, jsonify
import pandas as pd
import sqlite3 as sql
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/recommender",methods=["POST"])
def recommender():
    if request.method == "POST":
        genre = request.form["genre"]
        selected_range = request.form["year"]

        if selected_range == "1900-1950":
            year_range = range(1900, 1951)
        elif selected_range == "1950-2000":
            year_range = range(1950, 2001)
        elif selected_range == "2000-2023":
            year_range = range(2000, 2024)
        else:
            year_range = []
        
                
        conn = sql.connect("movies_db.db")

        c = conn.cursor()
        
        c.execute('''
            SELECT * FROM movies 
            WHERE genres LIKE ? AND title_year BETWEEN ? AND ?
            ORDER BY imdb_score DESC
        ''', ('%' + genre + '%', min(year_range), max(year_range)))
        

        filtered_movies = c.fetchall()
        

        return render_template('result.html', movies=filtered_movies, genre=genre, selected_range=selected_range)



@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/joinus")
def joinus():
    return render_template("joinus.html")

if __name__ == "__main__":
    app.run(debug=True  )
