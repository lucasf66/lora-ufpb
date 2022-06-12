#imports
import os
from sqlite3 import connect
import mysql.connector

class Database():
    def connect(self):
        self.host = os.getenv('SQL_HOST')
        self.user = os.getenv('SQL_USER')
        self.password = os.getenv('SQL_PASSWORD')
        self.database = os.getenv('SQL_DATABASE')
        return mysql.connector.connect(host=self.host,
                        user=self.user,
                        password=self.password, 
                        database=self.database)
    @staticmethod
    def insert(self,sql):
        connection = self.connect()
        cursor = self.connection.cursor()
        cursor.execute(sql)
        self.connect().commit()
        cursor.close()
    

