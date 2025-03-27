import os

from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


from pymongo.errors import ServerSelectionTimeoutError
from pymongo import MongoClient

from dotenv import load_dotenv

from models import book

load_dotenv()

app = Flask(__name__)

# ************************ IMPORTANT ****************************************
# mongodb credentials are currently being passed via env not git secrets
# ensure the database user has Atlas Admin access and that env includes
# values for the MONGO_USERNAME and MONGO_PASSWORD, feel free to update this
# ***************************************************************************

MONGO_USERNAME = os.getenv("MONGO_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD")


# -----mongo db set up-------
app.config["MONGO_URI"] = f"mongodb+srv://{MONGO_USERNAME}:{MONGO_PASSWORD}@cluster0.ndlv9.mongodb.net/BookStoreDB?retryWrites=true&w=majority&appName=Cluster0"

mongo = PyMongo(app)

# ping mongodb
try:
    mongo.cx.admin.command("ping")
    print("---- Connected to MongoDB ----")
except ServerSelectionTimeoutError:
    print("failed to connect to MongoDB")

# ----------
# database collection
books_collection = mongo.db.books


# -------- CRUD ---------

# HOMEPAGE ---tested: works ✔
@app.route("/")
def index():
    return render_template("index.html")


# VIEW BOOKS --- tested: works ✔
@app.route("/books/view")
def view_books():
    books = books_collection.find()
    book_list = [
        {"_id": str(book["_id"]),  # Convert _id to string
         "title": book["title"],
         "author": book["author"],
         "price": book["price"],
         "stock": book["stock"]
         }
        for book in books
    ]
    return render_template("books.html", books=book_list)


# ADD ---tested: works ✔
@app.route("/books/add", methods=["GET"])
def add_book_get():
    return render_template("add_book.html")


@app.route("/books/add", methods=["POST"])
def add_book_post():
    title = request.form.get("title")
    author = request.form.get("author")
    price = float(request.form.get("price"))
    stock = int(request.form.get("stock"))

    if not title or not author or not price or not stock:
        return jsonify({"error": "All fields are required"}), 400

    book_data = {
        "title": title,
        "author": author,
        "price": float(price),
        "stock": int(stock)
    }

    books_collection.insert_one(book_data)

    return redirect(url_for("view_books"))


# UPDATE --- tested: works ✔
@app.route("/books/update/<book_id>", methods=["GET"])
def update_book_get(book_id):
    book = books_collection.find_one({"_id": ObjectId(book_id)})

    if not book:
        return jsonify({"error": "Book not found"}), 404

    return render_template("update_book.html", book=book)



@app.route("/books/update/<book_id>", methods=["POST"])
def update_book_post(book_id):
    title = request.form.get("title")
    author = request.form.get("author")
    price = request.form.get("price")
    stock = request.form.get("stock")

    if not title or not author or not price or not stock:
        return jsonify({"error": "All fields are required"}), 400

    update_data = {
        "title": title,
        "author": author,
        "price": float(price),
        "stock": int(stock)
    }

    result = books_collection.update_one({"_id": ObjectId(book_id)}, {"$set": update_data})

    if result.modified_count:
        return redirect(url_for("view_books"))

    return jsonify({"error": "No changes were made"}), 400


# DELETE --- tested: works ✔
@app.route("/books/delete/<book_id>", methods=["POST"])
def delete_book(book_id):
    result = books_collection.delete_one({"_id": ObjectId(book_id)})

    if result.deleted_count:
        return redirect(url_for("view_books"))

    return jsonify({"error": "Book not found"}), 404

# -------------MAIN -------------------------


if __name__ == "__main__":
    app.run(debug=True)



