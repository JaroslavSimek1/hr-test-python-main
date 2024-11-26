class Genre:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Book:
    def __init__(self, id, title, description, cover_image_url, author_id, genre_id, price, is_available):
        self.id = id
        self.title = title
        self.description = description
        self.cover_image_url = cover_image_url
        self.author_id = author_id
        self.genre_id = genre_id
        self.price = price
        self.is_available = is_available


class Inventory:
    def __init__(self, id, book_id, stock):
        self.id = id
        self.book_id = book_id
        self.stock = stock


class Order:
    def __init__(self, id, book_id, quantity, order_date):
        self.id = id
        self.book_id = book_id
        self.quantity = quantity
        self.order_date = order_date
