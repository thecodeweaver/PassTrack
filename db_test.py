#!/usr/bin/python3
# Database test driver

from Database import *
from Account import *

db = Database("test.db")
my_acc = Account("root", "toor", "Superuser", "localhost")

db.create_account(my_acc)

read_acc = db.get_account("Superuser")

print("First account:")
print("Account name:", read_acc.get_name())
print("User name:", read_acc.get_user())
print("Password:", read_acc.get_pass())
print("Login URL:", read_acc.get_login_url())

my_acc.set_user("ubuntu")
my_acc.set_pass("ubuntu")
my_acc.set_login_url("10.10.13.37")

db.modify_account("Superuser", my_acc)

read_acc = db.get_account("Superuser")

print("\nSecond account:")
print("Account name:", read_acc.get_name())
print("User name:", read_acc.get_user())
print("Password:", read_acc.get_pass())
print("Login URL:", read_acc.get_login_url())

db.delete_account("Superuser")
db.close()