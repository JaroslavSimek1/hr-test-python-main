from connection_simulator import ConnectionSimulator

class AuthorData:
    def __init__(self, connection=None):
        if connection is None:
            self.connection = ConnectionSimulator()
            self.connection.connect() 
        else:
            self.connection = connection

    def create_author(self, name):
        query = "INSERT INTO authors (name) VALUES (%s) RETURNING id;"
        params = (name,)
        result = self.connection.execute_query(query, params)
        return result

    def get_author(self, author_id):
        query = "SELECT * FROM authors WHERE id = %s;"
        params = (author_id,)
        result = self.connection.execute_query(query, params)
        return result

    def update_author(self, author_id, name):
        query = "UPDATE authors SET name = %s WHERE id = %s;"
        params = (name, author_id)
        result = self.connection.execute_query(query, params)
        return result

    def delete_author(self, author_id):
        query = "DELETE FROM authors WHERE id = %s;"
        params = (author_id,)
        result = self.connection.execute_query(query, params)
        return result

class GenreData:
    def __init__(self, connection=None):
        if connection is None:
            self.connection = ConnectionSimulator()
            self.connection.connect()
        else:
            self.connection = connection

    def create_genre(self, name):
        query = "INSERT INTO genres (name) VALUES (%s) RETURNING id;"
        params = (name)
        result = self.connection.execute_query(query, params)
        return result

    def get_genre(self, genre_id):
        query = "SELECT * FROM genres WHERE id = %s;"
        params = (genre_id)
        result = self.connection.execute_query(query, params)
        return result

    def update_genre(self, genre_id, name):
        query = "UPDATE genres SET name = %s WHERE id = %s;"
        params = (name, genre_id)
        result = self.connection.execute_query(query, params)
        return result

    def delete_genre(self, genre_id):
        query = "DELETE FROM genres WHERE id = %s;"
        params = (genre_id)
        result = self.connection.execute_query(query, params)
        return result
    
class BookData:
    def __init__(self, connection=None):
        if connection is None:
            self.connection = ConnectionSimulator()
            self.connection.connect()
        else:
            self.connection = connection

    def create_book(self, title, description, cover_image_url, author_id, genre_id, price, is_available=True):
        query = """
            INSERT INTO books (title, description, cover_image_url, author_id, genre_id, price, is_available)
            VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id;
        """
        params = (title, description, cover_image_url, author_id, genre_id, price, is_available)
        result = self.connection.execute_query(query, params)
        return result

    def get_book(self, book_id):
        query = "SELECT * FROM books WHERE id = %s;"
        params = (book_id)
        result = self.connection.execute_query(query, params)
        return result

    def update_book(self, book_id, title=None, description=None, cover_image_url=None, author_id=None, genre_id=None, price=None, is_available=None):
        updates = []
        params = []

        if title:
            updates.append("title = %s")
            params.append(title)
        if description:
            updates.append("description = %s")
            params.append(description)
        if cover_image_url:
            updates.append("cover_image_url = %s")
            params.append(cover_image_url)
        if author_id:
            updates.append("author_id = %s")
            params.append(author_id)
        if genre_id:
            updates.append("genre_id = %s")
            params.append(genre_id)
        if price is not None:
            updates.append("price = %s")
            params.append(price)
        if is_available is not None:
            updates.append("is_available = %s")
            params.append(is_available)

        query = f"UPDATE books SET {', '.join(updates)} WHERE id = %s;"
        params.append(book_id)

        result = self.connection.execute_query(query, params)
        return result

    def delete_book(self, book_id):
        query = "DELETE FROM books WHERE id = %s;"
        params = (book_id)
        result = self.connection.execute_query(query, params)
        return result

class InventoryData:
    def __init__(self, connection=None):
        if connection is None:
            self.connection = ConnectionSimulator()
            self.connection.connect()
        else:
            self.connection = connection

    def create_inventory(self, book_id, stock):
        query = "INSERT INTO inventory (book_id, stock) VALUES (%s, %s) RETURNING id;"
        params = (book_id, stock)
        result = self.connection.execute_query(query, params)
        return result

    def get_inventory(self, inventory_id):
        query = "SELECT * FROM inventory WHERE id = %s;"
        params = (inventory_id)
        result = self.connection.execute_query(query, params)
        return result

    def update_inventory(self, inventory_id, stock):
        query = "UPDATE inventory SET stock = %s WHERE id = %s;"
        params = (stock, inventory_id)
        result = self.connection.execute_query(query, params)
        return result

    def delete_inventory(self, inventory_id):
        query = "DELETE FROM inventory WHERE id = %s;"
        params = (inventory_id)
        result = self.connection.execute_query(query, params)
        return result
