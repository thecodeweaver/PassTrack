class Account:
    username = None
    password = None
    account_name = None
    login_url = None

    def __init__(self, username, password, account_name, login_url):
        self.username = username
        self.password = password
        self.account_name = account_name
        self.login_url = login_url

    def get_user(self):
        return self.username

    def set_user(self, username):
        self.username = username

    def get_pass(self):
        return self.password

    def set_pass(self, password):
        self.password = password

    def get_name(self):
        return self.account_name

    def set_name(self, account_name):
        self.account_name = account_name

    def set_login_url(self, login_url):
        self.login_url = login_url

    def get_login_url(self):
        return self.login_url

    #def generate_password(self):
        # TODO