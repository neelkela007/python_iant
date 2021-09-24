import mysql.connector

class Work:
    def __init__(self, dbname):
        self.dbname = dbname
        self.con = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "neel",
            databse = self.dbname,
        )

    def create_table(self, query):
        cur = self.con.cursor()
        cur.execute(query)

    def insert_table(self, query):
        cur = self.con.cursor()
        cur.execute(query)

    def update_table(self, query):
        cur = self.con.cursor()
        cur.execute(query)

    def delete_data(self, query):
        cur = self.con.cursor()
        cur.execute(query)

    def delete_table(self, table_name):
        cur = self.con.cursor()
        tbl = "drop table {}".format(table_name)
        cur.execute(tbl)

    def delete_database(self, dname):
        cur = self.con.cursor()
        d = f"drop database {dname}"
        try:
            cur.execute(d)
        except:
            print("Invelid Query")

    def search(self, query):
        cur = self.con.cursor()
        cur.execute(query)

name = input("Enter Databse Name: ")
obj = Work(name)

q = input("Enter Databse query: ")
obj.delete_table("marks")

# insert into marks (gujarati, maths, english) values (30, 15, 33)
# insert into table_name (columns) values (data)
# drop table table_name
