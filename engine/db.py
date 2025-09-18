import csv
import sqlite3

con=sqlite3.connect('jarvis.db')
cursor=con.cursor()

#query="CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
#cursor.execute(query)

#query="INSERT INTO sys_command VALUES (null,'onenote','C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.EXE')"
#cursor.execute(query)
#con.commit()

#query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
#cursor.execute(query)

#ERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
#te(query)
#

#query="CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name VARCHAR(100),path VARCHAR(1000))"
#cursor.execute(query)

#query="INSERT INTO web_command VALUES (null,'youtube','https://www.youtube.com/')"
#cursor.execute(query)
#conn.commit()


#Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 30]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890', 'null')"
# cursor.execute(query)
# con.commit()

query = 'jeetu don'
query = query.strip().lower()

cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
results = cursor.fetchall()
print(results[0][0])

# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 31st columns
#desired_columns_indices = [0, 28, 29]
#
#with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#    csvreader = csv.reader(csvfile)
#    for row in csvreader:
#        if len(row) > max(desired_columns_indices):
#            selected_data = [row[i] for i in desired_columns_indices]
#            # Insert id (column 0), name (28), mobile_no (29)
#            cursor.execute(
#                "INSERT INTO contacts (id, name, mobile_no) VALUES (?, ?, ?);",
#                tuple(selected_data)
#            )
#        else:
#            print(f"Skipping row with insufficient columns: {row}")
#
#con.commit()
#con.close()


