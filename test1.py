
import os
import shutil
import mysql.connector
import random# <------ This is for generating random password


# for generating random password below three line is important
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 12
#p =  "".join(random.sample(s,passlen ))
# print(f"Your password is {p}")

############################################################################################
project_name = input("Enter your project name :- ")




project_pass = "".join(random.sample(s,passlen ))
mysql_pass = "".join(random.sample(s,passlen ))

print(f"Your project name is :-  {project_name}")
print(f"Your project password is :- {project_pass}")
print(f"Your mysql password is :- {mysql_pass}")


print("Creating a Directory")
os.mkdir('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name)
os.mkdir('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name+'/dev')
os.mkdir('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name+'/qa')
os.chmod('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name+'/dev',0o777)
os.chmod('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name+'/qa',0o777)

if os.path.exists('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name):
    print("Directory created successfully")
    os.listdir('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name)
else:
    print("Failed to create Directory")

print('Copying the Gitlab')
shutil.copytree("/Users/sarfaraz/Downloads/gitlab", '/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name+'/gitlab')

if os.path.exists('/Users/sarfaraz/PycharmProjects/pythontesting/'+project_name+'/gitlab'):
    print("Successfully copied the gitlab file")
else:
    print("Failed to copy")

print("Editing the gitlab file")
s = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php").read()
s = s.replace('bannershop', project_name)
f = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php", 'w')
f.write(s)
f.close()

s = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php").read()
s = s.replace('fohC0oobao3i', project_pass)
f = open("/Users/sarfaraz/PycharmProjects/pythontesting/testing/gitlab/deploy.php", 'w')
f.write(s)
f.close()

print(os.listdir('/Users/sarfaraz/PycharmProjects/pythontesting/testing'))

######################################

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE "+project_name+'_dev')
mycursor.execute("CREATE DATABASE "+project_name+'_qa')



