import mysql.connector

__cnx=None
def get_connection():
    global __cnx
    if __cnx is None:
        __cnx=mysql.connector.connect(user='root',password='netflix@11',
                                      host='localhost',database='grocery')



    return __cnx



