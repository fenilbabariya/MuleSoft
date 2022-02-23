# Import Required Files
from connection import *

# Database Creation
try:
    name = input("Enter Movie Name: ")
    actor = input("Enter Actor Name: ")
    actress = input("Enter Actress Name: ")
    director = input("Enter Director Name: ")
    year = int(input("Enter Release Year: "))
    
    # Insert Query to insert data into table
    conn.execute("insert into Movies (moviename,actor,actress,director,year) values (?,?,?,?,?)",(name,actor,actress,director,year))
    # Commit() to commit data in database
    conn.commit()
    print("Data Inserted")
except:
    print("Data Insertion Failed")