# Install the mysql connector on remote machine
# sudo apt-get install python3-mysql.connector -y
# sudo apt-get install python3-pip -y
import os


print(os.system('ssh root@192.168.15.98 python3 < /Users/sarfaraz/PycharmProjects/pythontesting/test2.py --opt newtest'))
#print(os.system('cat /Users/sarfaraz/PycharmProjects/pythontesting/test2.py | ssh root@192.168.15.98 python3 -' ))