import cmd
import getpass
import secrets

from Database import *
from Account import *
from wordlist import *

class Shell(cmd.Cmd):
    # Class for the PassTrack command shell
    intro = """
     ███████████                            ███████████                              █████     
░░███░░░░░███                          ░█░░░███░░░█                             ░░███      
 ░███    ░███  ██████    █████   █████ ░   ░███  ░  ████████   ██████    ██████  ░███ █████
 ░██████████  ░░░░░███  ███░░   ███░░      ░███    ░░███░░███ ░░░░░███  ███░░███ ░███░░███ 
 ░███░░░░░░    ███████ ░░█████ ░░█████     ░███     ░███ ░░░   ███████ ░███ ░░░  ░██████░  
 ░███         ███░░███  ░░░░███ ░░░░███    ░███     ░███      ███░░███ ░███  ███ ░███░░███ 
 █████       ░░████████ ██████  ██████     █████    █████    ░░████████░░██████  ████ █████
░░░░░         ░░░░░░░░ ░░░░░░  ░░░░░░     ░░░░░    ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ 
                                                                                         
    """
    prompt = ">"

    db = Database("passtrack.db")

    def do_create(self, line):
        """create
        Create a new account entry"""
        account_name = input("Please enter the account name: ")
        username = input("Please enter the username: ")
        password = getpass.getpass("Please enter your password: ")
        login_url = input("Please input the login URL: ")

        # TODO: Encrypt the password before storing it in the database

        acc = Account(username, password, account_name, login_url)

        self.db.create_account(acc)

    def do_read(self, account_name):
        """read [account name]
        Print out the information for an exisiting account entry"""
        self.db.open("passtrack.db")
        acc = self.db.get_account(account_name)

        print("Information for %s: " % account_name)
        print("Username: %s" % acc.get_user())
        print("Password: %s" % acc.get_pass())
        print("Login URL: %s" % acc.get_login_url())

        self.db.close()

    def do_update(self, account_name):
        """update [account name]
        Update an existing account entry"""
        self.db.open("passtrack.db")

        username = input("Please enter the new username: ")
        password = getpass.getpass("Please enter your new password: ")
        login_url = input("Please input the new login URL: ")

        # TODO: Encrypt the password before storing it in the database

        acc = Account(username, password, account_name, login_url)

        self.db.modify_account(account_name, acc)

        self.db.close()

    def do_delete(self, account_name):
        """delete [account name]
        Delete an account entry"""
        self.db.open("passtrack.db")

        self.db.delete_account(account_name)

        self.db.close()

    def do_generate(self, line):
        """generate
        Generate a secure password using Diceware
        """
        print("Generating password:...")

        password = ""
        for i in range(0, 3):
            number = ""
            for j in range(0, 5):
                secret = 0
                while secret == 0:
                    secret = secrets.randbelow(6)

                number = number + str(secret)
                # print("DEBUG: number = " + number)

            password = password + wordlist.get(number).capitalize()

        print("Your password is: " + password);

    def do_list(self, line):
        """list
        Print out all the accounts stored in the database"""
        self.db.open("passtrack.db")
        accounts = self.db.get_all_accounts()
        
        for i in accounts:
            print("Account name: " + i[0])
            print("Account username: " + i[1])
            print("Account password: " + i[2])
            print("Login URL: " + i[3])
            print("\n")
        
        self.db.close()

    def do_exit(self, line):
        """exit
        Quit the program"""
        return True