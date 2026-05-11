from datetime import datetime

class User:
    def __init__(self, username, mail, password):
        self.username = username
        self._email = mail          # protected data attribute
        self.__password = password  # to make it private so it cant be accessed

    def say_hi_to_user(self, user):
        print(
            f"Sending message to {user.username}: \nHi {user.username}\nit's {self.username}"
            )
    
    # Properties (recommended) way to control access inpython
    
    # getter property to access protected data
    @property    
    def email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    # setter property to modify the value of the protected data
    @email.setter
    def email(self, new_email):
        if "@" in new_email:
            self._email = new_email

    def get_password(self):
        return self.__password

user1 = User("dantheman", "dan@gmail.com", "123")
user2 = User("batman", "bat@outlook.com", "abc")

# user1.say_hi_to_user(user2)
print(user1.email())


