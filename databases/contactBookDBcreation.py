import sqlite3

# connect to db & create it if not already made
connection = sqlite3.connect("contacts.db")

# Create cursor to manipulate db
cursor = connection.cursor()

# Create pokemon data table
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contact_name TEXT, 
    contact_number INT
)
''')

# Commit changes
connection.commit()

# Close connection with database
connection.close()