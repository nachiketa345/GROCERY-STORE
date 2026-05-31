import mysql.connector

__cnx=None
def get_connection():
    global __cnx
    if __cnx is None:
        __cnx=mysql.connector.connect(user='root',password='netflix@11',
                                      host='localhost',database='grocery')



    return __cnx


def get_connection_pool():
    pool = mysql.connector.pooling.MySQLConnectionPool(pool_name="mypool",
                                                       pool_size=5,
                                                       user='root',
                                                       password='netflix@11',
                                                       host='localhost',
                                                       database='grocery')
    return pool.get_connection()
