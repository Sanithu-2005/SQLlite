import sqlite3

#The following is Database Def

#connect to database (cretaes film.db if it doesn't exist)
db=sqlite3.connect("film.db") #connects to the database by the name film.db or if it doesn't exist then it will create it
cursor=db.cursor() 
print("Database Connected")

#DDL example below/Create Table #The below command creates a table called Film inside the .db file if it already doesn't exist
sql='''
CREATE TABLE IF NOT EXISTS Film( 
     FilmID INTEGER PRIMARY KEY,
     Title TEXT,
     Genre TEXT,
     Year INTEGER
     );
'''
cursor.execute(sql)
db.commit()
print("Table created!")

#---------------------------------------------------------

#Insert sample records
#The following (insert) is Database Manipulation
cursor.execute("""INSERT INTO Film (Title,Genre,Year)
                  VALUES ("Wild","Drama",2014);""") #you can either use a variable or just directly use the commands
#copy from MySQL to SQLlite
cursor.execute("""INSERT INTO Film (Title,Genre,Year)
                  VALUES ("The Lion King","Drama",1994);""")
cursor.execute("""INSERT INTO Film (Title,Genre,Year)
                  VALUES ("Gone Girl","Drama",2014);""")
db.commit()
print("Sample records inserted!")

#The code as it is upto this point will keep creating without checking so that need addressing
#Parameterized insert
#Assigned as varaibles so rather then line by line we can do all at once

film = ("Django Unchained","Western",2012)#still one record
cursor.execute("INSERT INTO Film (Title,Genre,Year) VALUES (?,?,?);",film)

#To insert many records do the following
films_many=[
    ("Selma","Drama",2014),
    ("Boyhood","Family",2014)
]
cursor.executemany("INSERT INTO Film (Title,Genre,Year) VALUES (?,?,?);",films_many)
db.commit()
print("Parameterized records inserted")

# Select all records
cursor.execute("SELECT * FROM Film")
print("All films:")
for row in cursor.fetchall():
    print(row)

#SELECT TITLE FROM Film if I want to select just TITLE
# Update a record
cursor.execute("UPDATE Film SET Year = 2013 WHERE Title = 'Wild' ")
db.commit()
print("Record updated")

#To see if you have updated
cursor.execute("SELECT * FROM Film")
print("All films:")
for row in cursor.fetchall():
    print(row)
    
#Delete Records
cursor.execute("DELETE FROM Film WHERE Year = 1994")
db.commit()
print("Record(s) deleted!")

#Close DB
db.close()
print("Database closed!")
