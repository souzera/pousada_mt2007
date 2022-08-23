import psycopg2

class ConnectDataBase:

    def __init__(self):
        self._connect = psycopg2.connect(
            host="localhost",
            database="mt2007_db",
            user="postgres",
            password="1969"
        )

    def get_instance(self):
        return self._connect