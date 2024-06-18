import mysql.connector
from mysql.connector import Error

import mysql.connector
from mysql.connector import Error


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            port=3304,
            database='swedish',
            user='root',
            password='iskambmw320'
        )
        if connection.is_connected():
            cursor = connection.cursor()
            return connection, cursor
        else:
            print("Connection failed")

    except Error as e:
        print("Error while connecting to MySQL", e)
        return None, None


def insert_to_database(filename, freemansCode, histogram_count, connection, cursor):
    histogram_count = [int(value) for value in histogram_count]
    freeman = prepare_import_data(freemansCode)
    sql = """
    INSERT INTO leaf2files 
   (fileName, freemansCode, hist0, hist1, hist2, hist3, hist4, hist5, hist6, hist7)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        filename,
        freeman,
        histogram_count[0],
        histogram_count[1],
        histogram_count[2],
        histogram_count[3],
        histogram_count[4],
        histogram_count[5],
        histogram_count[6],
        histogram_count[7]
    )

    try:
        cursor.execute(sql, values)
        connection.commit()
        print("Record inserted successfully into leaf2files table")
    except Error as e:
        print(f"Failed to insert record into MySQL table {e}")


def prepare_import_data(int_array):
    str_list = [str(code) for code in int_array]
    string = ', '.join(str_list)
    return string
