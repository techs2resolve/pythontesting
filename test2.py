# s = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php").read()
# s = s.replace('trustquid', 'testing')
# f = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php", 'w')
# f.write(s)
# f.close()
#
# s = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php").read()
# s = s.replace('fohC0oobao3i', 'testing')
# f = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php", 'w')
# f.write(s)
# f.close()

import shutil
import os
import mysql.connector

test = input("Enter the database name :- ")
#test = 'testing2'
testpass = 'test123'

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root"
  )

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE "+test+'_dev')
mycursor.execute("CREATE DATABASE "+test+'_qa')
mycursor.execute("CREATE USER "+test+'@localhost IDENTIFIED BY '+"'"+testpass+"';")
mycursor.execute("GRANT ALL PRIVILEGES ON "+test+'_dev'".* "+'TO '+test+"@localhost;")
mycursor.execute("GRANT ALL PRIVILEGES ON "+test+'_qa'".* "+'TO '+test+"@localhost;")
mycursor.execute("FLUSH PRIVILEGES;")
mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)


# shutil.copytree('/Users/sarfaraz/Downloads/gitlab', '/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab')
# # shutil.copy('/Users/sarfaraz/Downloads/gitlab', '/Users/sarfaraz/PycharmProjects/pythontesting/testing')
# print(os.listdir('/Users/sarfaraz/PycharmProjects/pythontesting/testing'))
# test = 'testing'
# print("CREATE DATABASE "+test+'_dev;')
#
# print("CREATE USER "+test+'@localhost IDENTIFIED BY '+"'"+testpass+"';")
#
# print("GRANT ALL PRIVILEGES ON "+test+'_dev'".* "+'TO '+test+"@localhost;")
# print("FLUSH PRIVILEGES;")