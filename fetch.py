# Import Required Files
from connection import *

# Database Creation
try:
    # Cursor that stores data
    cursor = conn.execute('select * from Movies')
    # Fetch all method to fetch data from cursor
    rows = cursor.fetchall()
    for details in rows:
        print(details)

except:
    print("Error in Fetch")