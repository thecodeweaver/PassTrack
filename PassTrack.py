#!/usr/bin/python3

from Shell import *
from Database import *

import os.path
import hashlib
import sys
import getpass

if __name__ == "__main__":
    # Check for database file
    if not os.path.exists("shadow"):
        # Create database file and prompt user for master password
        password = getpass.getpass("Please enter a master password: ") 

        # Hash password and store it in a file which will be used as an encryption key
        hash = hashlib.md5(bytes(password, 'utf-8')).hexdigest()
        fh = open("shadow", "w")
        fh.write(hash)
        fh.close()

        db = Database("passtrack.db")
        db.create_table()
        db.close()
        print("Database created!")

    # Prompt user for master password to access the program
    password = getpass.getpass("Please enter your master password: ")
    password_hash = hashlib.md5(bytes(password, 'utf-8')).hexdigest()

    # Read hash from file and compare it with the entered password
    fh = open("shadow", "r")
    stored_hash = fh.read(32)
    fh.close()

    if (stored_hash != password_hash):
        sys.exit("Incorrect password, exiting...")
        
    # Begin the command loop
    Shell().cmdloop()
