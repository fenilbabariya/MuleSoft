# Import Required Libraries
from sqlite3 import *

# Database and Table Creation
try:
    conn = connect("dbmovies.db")
    # Table Creation Query
    conn.execute("create table if not exists Movies (id integer primary key autoincrement, moviename text, actor text, actress text, director text, year integer)")
    print("Database and Table Created")
except:
    print("Error in Database or Table Creation")