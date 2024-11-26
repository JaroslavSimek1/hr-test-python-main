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