from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data - initially empty
books = []

# Counter for generating unique IDs
next_id = 1

# Create operation - Add a new book
@app.route('/books', methods=['POST'])
def add_book():
    global next_id
    data = request.json
    book = {
        'id': next_id,
        'book_name': data['book_name'],
        'author': data['author'],
        'publisher': data['publisher']
    }
    books.append(book)
    next_id += 1
    return jsonify({'message': 'Book added successfully', 'book': book}), 201

# Read operation - Retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Read operation - Retrieve a specific book by ID
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    else:
        return jsonify({'message': 'Book not found'}), 404

# Update operation - Update a book by ID
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.json
    for book in books:
        if book['id'] == book_id:
            book['book_name'] = data['book_name']
            book['author'] = data['author']
            book['publisher'] = data['publisher']
            return jsonify({'message': 'Book updated successfully', 'book': book})
    return jsonify({'message': 'Book not found'}), 404

# Delete operation - Delete a book by ID
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    initial_length = len(books)
    books = [book for book in books if book['id'] != book_id]
    if len(books) < initial_length:
        return jsonify({'message': 'Book deleted successfully'}), 200
    else:
        return jsonify({'message': 'Book not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
