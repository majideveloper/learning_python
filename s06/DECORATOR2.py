def star(func):
    def inner(*x,**y):
        print("*" * 20 )
        func(*x , ** y)
        print("*" * 20 )
    return inner

@star
def msg(name):
    print("I am " + name)

msg("MAJID")