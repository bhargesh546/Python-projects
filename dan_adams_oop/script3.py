from datetime import datetime

# Traditional approach of accessing and updating the values of attriibutes (Java approach)
# This is done by making the data private and using getters and setters methods

class User:
    def __init__(self, username, email, password):
        self.username = username
        self._email = email             # protected
        self.__password = password      # private
    
    def clean_eamil(self):
        return self._email.strip().lower()
    
    def get_email(self):
        print(f"Email accessed at {datetime.now()}")
        return self._email
    
    def set_email(self, new_email):
        self._email = new_email

    def say_hi_to_user(self, user):
        print(f"Sending message to {user.username}: \nHi {user.username}, it's {self.username}")
        
user1 = User("dantheman", "Dan@gmail.com", "123")
user2 = User("Batman", "bat@outlook.com", "abc")

user1.say_hi_to_user(user2)
user1.clean_eamil()
print(user1.get_email())
