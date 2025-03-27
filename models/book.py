class Book:
    def __init__(self, _id, title, author, price, stock):
        self._id = _id  # Include the _id field from MongoDB
        self.title = title
        self.author = author
        self.price = price
        self.stock = stock


# fetches book data from mongo db --- this is unused
def get_book_from_db(mongo):
    books_collection = mongo.db.books
    books_data = books_collection.find()
    books_list = []

    for book_data in books_data:
        books_list.append(Book(book_data["title"], book_data["author"], book_data["price"], book_data["stock"]))

    return books_list


# inserts sample book data to mongo db --- only used for sample
def insert_example_books(mongo):
    books = [
        {"title": "Isekai no Owl", "author": "Mitch Bresette", "price": 19.99, "stock": 5},
        {"title": "Mirai no Owl", "author": "Mitch Bresette", "price": 19.99, "stock": 4},
        {"title": "Stranger Days", "author": "Mitch Bresette", "price": 29.99, "stock": 2}
    ]

    books_collection = mongo.db.books


    # checks that the inserted data is not the same as the existing data, replaced with unique=True below
    '''
    for book in books:
        existing_book = books_collection.find_one({"title": book["title"], "author": book["author"], "price": book["price"], "stock": book["stock"] })

        if not existing_book:
            books_collection.insert_one(book)
        else:
            print("Error Book Already Exists")
    '''

    # updated version of previous
    books_collection.create_index(["title", "author", "price", "stock"], unique=True)

    for book in books:
        try:
            books_collection.insert_one(book)
        except Exception as e:
            print(f"Error {e}")


