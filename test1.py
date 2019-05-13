
import os
import random  # <------ This is for generating random password

# for generating random password below three line is important
s = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
passlen = 12
p =  "".join(random.sample(s,passlen ))
# print(f"Your password is {p}")


project_pass = "".join(random.sample(s,passlen ))
mysql_pass = "".join(random.sample(s,passlen ))

print(f"Your project password is {project_pass}")
print(f"Your mysql password is {mysql_pass}")


print(project_pass)