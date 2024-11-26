class ConnectionSimulator:
    def __init__(self):
        self._is_connected = False

    @property
    def is_connected(self):
        return self._is_connected

    def connect(self):
        if not self._is_connected:
            self._is_connected = True

        return True

    def disconnect(self):
        if self._is_connected:
            self._is_connected = False

        return True

    def execute_query(self, query, params=None):
        if not self._is_connected:
            raise ConnectionError("Not connected to a database")

        if not isinstance(query, str):
            raise ValueError("Query must be a string")

        if params:
            # map params to query...
            pass

        return []
