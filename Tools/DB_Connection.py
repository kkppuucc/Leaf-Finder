import mysql.connector
from mysql.connector import Error

def connect_to_database():
    connection = None  # Initialize connection variable
    cursor = None  # Initialize cursor variable
    try:
        connection = mysql.connector.connect(
            host='localhost',  # e.g., 'localhost'
            port=3304,
            database='swedish',  # e.g., 'swedish'
            user='root',  # e.g., 'root'
            password='iskambmw320'  # e.g., 'password'
        )

        if connection.is_connected():
            db_info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_info)
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)

            # List all databases
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            print("Available databases:")
            for db in databases:
                print(db[0])

    except Error as e:
        print("Error while connecting to MySQL", e)
    finally:
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            print("MySQL connection is closed")

if __name__ == '__main__':
    connect_to_database()
