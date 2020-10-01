# Import requirements
from flask import Flask, request, jsonify

app = Flask(__name__)

# The list of books in dict format
books_list = [
    {
        "id": 0,
        "author": "Chinua Achebe",
        "language": "English",
        "title": "Things Fall Apart",
    },
    {
        "id": 1,
        "author": "Hans Christian Andersen",
        "language": "Danish",
        "title": "Fairy Tales",
    },
    {
        "id": 2,
        "author": "Samuel Beckett",
        "language": "French, English",
        "title": "Molloy, Malone Dies, The Unnamable, The Trilogy",
    }
]

# Set location to localhost/books, available methods are GET and POST
@app.route('/books', methods=['GET', 'POST'])

def books():
    if request.method == 'GET':
        if len(books_list) > 0:
            return jsonify(books_list)  # Convert dict list to .json format
        else:
            'Nothing found', 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_lang = request.form['language']
        new_title = request.form['title']
        iD = books_list[-1]['id']+1  # Automatically set the id as the lowest available num

        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_lang,
            'title': new_title,
        }
        books_list.append(new_obj)
        return jsonify(books_list), 201  # Show the user the book was added


if __name__ == '__main__':
    app.run()
