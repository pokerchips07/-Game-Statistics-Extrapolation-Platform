
import sqlite3

conn = sqlite3.connect("game_stats.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS player_stats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    player_name TEXT,
    score INTEGER,
    kills INTEGER,
    assists INTEGER
)
''')

conn.commit()
conn.close()
