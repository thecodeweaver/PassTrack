import sqlite3
import os.path

from Account import *

class Database:
    # Database entry format:
    # account name, username, password, login URL

    connection = None
    cursor = None

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.database_name = database_name
        self.cursor = self.connection.cursor()

    def create_table(self):
        self.cursor.execute("CREATE TABLE Accounts (account_name TEXT, username TEXT, password BLOB, login_url TEXT)")
        self.connection.commit()        

    def open(self, database_name):
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_account(self, acc):
        query = "INSERT INTO Accounts VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (acc.get_name(), acc.get_user(), acc.get_pass(), acc.get_login_url()))
        self.connection.commit()

    def get_account(self, account_name):
        query = "SELECT username FROM Accounts WHERE account_name = ?"
        username = self.cursor.execute(query, (account_name,)).fetchall()[0][0]

        query = "SELECT password FROM Accounts WHERE account_name = ?"
        password = self.cursor.execute(query, (account_name,)).fetchall()[0][0]

        query = "SELECT login_url FROM Accounts WHERE account_name = ?"
        login_url = self.cursor.execute(query, (account_name,)).fetchall()[0][0]

        self.connection.commit()

        acc = Account(username, password, account_name, login_url)
        
        return acc

    def modify_account(self, account_name, acc):
        query = "UPDATE Accounts SET username = ? WHERE account_name = ?"
        self.cursor.execute(query, (acc.get_user(), account_name))

        query = "UPDATE Accounts SET password = ? WHERE account_name = ?"
        self.cursor.execute(query, (acc.get_pass(), account_name))

        query = "UPDATE Accounts SET login_url = ? WHERE account_name = ?"
        self.cursor.execute(query, (acc.get_login_url(), account_name))

        self.connection.commit()

    def delete_account(self, account_name):
        query = "DELETE FROM Accounts WHERE account_name = ?"
        self.cursor.execute(query, (account_name,))
        self.connection.commit()

    def close(self):
        self.connection.close()
    
    def get_all_accounts(self):
        query = "SELECT * FROM Accounts"
        self.cursor.execute(query)
        acc_list = self.cursor.fetchall()
        self.connection.commit()

        return acc_list
