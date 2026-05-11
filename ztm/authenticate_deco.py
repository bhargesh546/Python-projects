# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:

def authenticated(func):
    def wrapper_fun(*args, **kwargs):
        if args[0]["valid"]:
            func(*args, **kwargs)
        else:
            print("Invalid user")
    return wrapper_fun

user1 = {
    "name": 'Michael Scott',
    "valid": False
}

@authenticated
def message_friends(user):
    print('message has been sent')

message_friends(user1)