paswords = {"majid":"1234", "ali":"majid123", "mehdi":"112233"}
blacklist = {"ali"}
from functools import wraps
def ban(func):
    @wraps(func)
    def inner (*args,**kwargs):
        if args[0] in blacklist:
            print("This user is blocked!!!!")
        else:
            func(*args, ** kwargs)
    return inner
@ban
def print_password(username):
    print(username , ":" , paswords[username])
@ban
def change_password(username , new_password):
    paswords[username] = new_password
    print(username , ":" , new_password)

print_password("ali")
change_password("ali","8585")
print(paswords)