# Contains all your sql queries.

# Drop Queries

"""
Drop queries for all tables.
"""

songplays_drop = "DROP TABLE IF EXISTS songplays"
users_drop     = "DROP TABLE IF EXISTS users"
songs_drop     = "DROP TABLE IF EXISTS songs"
artists_drop   = "DROP TABLE IF EXISTS artists"
time_drop      = "DROP TABLE IF EXISTS time"

# Create Queries

"""
Create queries for all tables.
"""

songplays_tbl = ("CREATE TABLE IF NOT EXISTS songplays (songplay_id SERIAL PRIMARY KEY, start_time VARCHAR, user_id VARCHAR, level VARCHAR, song_id VARCHAR, artist_id VARCHAR, session_id INT, location VARCHAR, user_agent VARCHAR)")
users_tbl     = ("CREATE TABLE IF NOT EXISTS users (user_id VARCHAR, first_name VARCHAR, last_name VARCHAR, gender VARCHAR, level VARCHAR)")
songs_tbl     = ("CREATE TABLE IF NOT EXISTS songs (song_id VARCHAR, title VARCHAR, artist_id VARCHAR, year INT, duration NUMERIC)")
artists_tbl   = ("CREATE TABLE IF NOT EXISTS artists (artist_id VARCHAR, name VARCHAR, location VARCHAR, latitude NUMERIC, longitude NUMERIC)")
time_tbl      = ("CREATE TABLE IF NOT EXISTS time (start_time VARCHAR, hour INT, day INT, week INT, month INT, year int, weekday VARCHAR)")

# INSERT Queries

"""
Insert queries for all tables.
"""

songplays_insert = ("INSERT INTO songplays (start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
users_insert     = ("INSERT INTO users     (user_id, first_name, last_name, gender, level) VALUES (%s, %s, %s, %s, %s)")
songs_insert     = ("INSERT INTO songs     (song_id, title, artist_id, year, duration) VALUES (%s, %s, %s, %s, %s)")
artists_insert   = ("INSERT INTO artists   (artist_id, name, location, latitude, longitude) VALUES (%s, %s, %s, %s, %s)")
time_insert      = ("INSERT INTO time      (start_time, hour, day, week, month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s)")

# Find Songs

song_select = ("SELECT songs.song_id, artists.artist_id FROM (songs \
                JOIN artists ON songs.artist_id = artists.artist_id) \
                ")

# List of tables for create/drop

create_stmts = [songplays_tbl, users_tbl, songs_tbl, artists_tbl, time_tbl]
drop_stmts   = [songplays_drop, users_drop, songs_drop, artists_drop, time_drop]