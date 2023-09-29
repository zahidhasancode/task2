

# backend/database.py
import sqlite3

def create_database():
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY,
            title TEXT,
            author TEXT,
            year INTEGER
        )
    ''')
    conn.commit()
    conn.close()

def insert_book(title, author, year):
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()

def get_books():
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    conn.close()
    return books

def update_book(id, title, author, year):
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE books SET title=?, author=?, year=? WHERE id=?", (title, author, year, id))
    conn.commit()
    conn.close()

def delete_book(id):
    conn = sqlite3.connect('mydb.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM books WHERE id=?", (id,))
    conn.commit()
    conn.close()
