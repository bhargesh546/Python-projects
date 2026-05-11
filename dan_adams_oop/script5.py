# Static attributes - It belongs to the class itself and not to any specific instance of the class, and only one copy in the class

class User:
    user_count = 0

    def __init__(self, username, email):
        self.username = username
        self.email = email
        User.user_count += 1

    def display_user(self):
        print(f"Username: {self.username}, Email: {self.email}")

user1 = User("dantheman", "dan@gmail.com")
user2 = User("sally123", "sally@gmail.com")

print(User.user_count)