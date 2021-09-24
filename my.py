# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="neel",
#   database="sys"
# )

# cur = mydb.cursor()

# query = "show table"
# cur.execute(query)

# for i in cur:
#     print(i)

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="neel",
    database="mysql"
)

mycursor = mydb.cursor()
mycursor.execute("Show databases")

for i in mycursor:
    print(i)
