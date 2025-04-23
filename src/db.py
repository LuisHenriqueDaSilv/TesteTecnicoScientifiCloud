import sqlite3
dbConnection =  sqlite3.connect("./data/database.db")
dbCursor = dbConnection.cursor()