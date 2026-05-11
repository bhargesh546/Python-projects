# Properties is more pythonic or current recommended approach 

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email             
        self.password = password

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, new_email):
        self._email = new_email

user1 = User("dantheman", "Dan@gmail.com", "123")