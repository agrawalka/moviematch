from flask import Flask,render_template,request,jsonify
import pandas as pd

import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/recommender",methods=["POST"])
def recommender():
    if request.method == "POST":
        genre = request.form["genre"]
        year = request.form["year"]

        # opening the dataset and finding the movies with specefic genres and year enterd by user
        with open("movie_metadata.csv","r", encoding="utf8") as cv:
            csv_rdr=csv.reader(cv)
            next(csv_rdr)

            filtered_movies=[]

            for row in csv_rdr:
                if genre in row[4] and year == row[12] :
                    filtered_movies.append(row)

        return render_template('result.html', movies=filtered_movies)

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




