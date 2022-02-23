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

    # Select data based on actorm name
    print("Fetch movie based on actor name")
    cursor = conn.execute("select * from Movies where actor='Aamir Khan'")
    # Fetch all method to fetch data from cursor
    rows = cursor.fetchall()
    for details in rows:
        print(details)

except:
    print("Error in Fetch")