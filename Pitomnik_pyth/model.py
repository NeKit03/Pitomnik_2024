import mysql.connector
import datetime
from functools import wraps


cursor=None




class DataBase_Pitomnik:
    def __init__(self):
        try:
            self.cnx=mysql.connector.connect(user='nikita', password='217455', host='localhost', port=3307, database='humanfriends')
            self.cursor=self.cnx.cursor()
            self.animal=None
            print("Connection successful!")
        except mysql.connector.Error as err:
            print("Failed to connect to MySQL: {}".format(err))
        

    def query_MySQL(self, query: str, *args): 
        return self.cursor.execute(query, *args)
    
    def query_MySQL_into(self,query:str,args:list[str]):
        self.cursor.execute(query,args)
        self.cnx.commit()

    def save_change(self):
        self.cnx.commit()
    
        

