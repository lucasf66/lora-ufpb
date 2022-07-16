#imports
from multiprocessing import connection
import os
from sqlite3 import connect
import mysql.connector
from dotenv import load_dotenv
load_dotenv()


class Database():
    
    ## Chama a conexão com o banco
    def connect():
        host = os.getenv('SQL_HOST')
        user = os.getenv('SQL_USER')
        password = os.getenv('SQL_PASSWORD')
        database = os.getenv('SQL_DATABASE')
        return mysql.connector.connect(host=host,
                        user=user,
                        password=password, 
                        database=database)                        
    
    ## Faz a inserção de uma sql querry
    @classmethod
    def insert(cls,sql):
        connection = cls.connect()
        cursor = connection.cursor()
        cursor.execute(sql)
        connection.commit()
        cursor.close()

