import sqlite3 as sql
import csv

conn = sql.connect('movies_db.db')

cursor = conn.cursor()

# cursor.execute('CREATE TABLE movies (movie_title TEXT, genres TEXT,title_year TEXT,imdb_score TEXT,actor_1_name TEXT,actor_2_name TEXT,actor_3_name TEXT,language TEXT, country TEXT)')


# with open('movie_metadata.csv', 'r', encoding="utf8") as file:
#     csv_data = csv.reader(file)
#     next(csv_data)  # Skip the header row if it exists

#     for row in csv_data:
#         # Insert each row into the table
#         cursor.execute('''
#             INSERT INTO movies (movie_title, genres,title_year,imdb_score,actor_1_name,actor_2_name,actor_3_name,language, country)
#             VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
#         ''', row)
        
# print("inserted successfully")

# cursor.execute("CREATE INDEX if not exists idx_movies_imdb_score ON movies (imdb_score)")

# conn.commit()
# conn.close()
