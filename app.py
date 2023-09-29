

# backend/app.py
from flask import Flask, request, jsonify
from database import create_database, insert_book, get_books, update_book, delete_book

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is the backend!'

@app.route('/add_book', methods=['POST'])
def add_book():
    data = request.get_json()
    title = data['title']
    author = data['author']
    year = data['year']
    insert_book(title, author, year)
    return jsonify({"message": "Book added successfully"})

@app.route('/get_books', methods=['GET'])
def get_all_books():
    books = get_books()
    return jsonify(books)

@app.route('/update_book/<int:id>', methods=['PUT'])
def update_a_book(id):
    data = request.get_json()
    title = data['title']
    author = data['author']
    year = data['year']
    update_book(id, title, author, year)
    return jsonify({"message": f"Book with ID {id} updated successfully"})

@app.route('/delete_book/<int:id>', methods=['DELETE'])
def delete_a_book(id):
    delete_book(id)
    return jsonify({"message": f"Book with ID {id} deleted successfully"})

if __name__ == '__main__':
    create_database()
    app.run(debug=True)

