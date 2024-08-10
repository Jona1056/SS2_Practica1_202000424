import pyodbc

class DatabaseConnection:
    _instance = None

    def __new__(cls):
        # Configuración del servidor y base de datos
      
        database = 'master'  # La base de datos a la que te quieres conectar
        
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
            try:
                cls._instance.conn =pyodbc.connect(r'Driver=SQL Server;Server=.\SQLEXPRESS;Database=SEMI2;Trusted_Connection=yes;')
                print("Conexión exitosa a SQL Server")
            except Exception as e:
                print("Error al conectar a SQL Server")
                print(e)
                cls._instance = None
        return cls._instance

    def get_connection(self):
        return self.conn

    def execute_query(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            self.conn.commit()
            return True, "Query ejecutado correctamente"
        except Exception as e:
            return False, e
    def execute_query_data(self, query):
        try:
            cursor = self.conn.cursor()
            result = cursor.execute(query)
            self.conn.commit()
            return result, False
        except Exception as e:
            
            return e, True
        

    def close_connection(self):
        if self.conn:
            self.conn.close()
            print("Conexión cerrada")
            self.conn = None
            
    def fetch_data(self, query):
        try:
            cursor = self.conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows, None
        except Exception as e:
            return None, e