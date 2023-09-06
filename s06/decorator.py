def dash(func):
    def inner(*x,**y):
        print("-" * 20 )
        func(*x , ** y)
        print("-" * 20 )
    return inner
def plus(func):
    def inner(*x,**y):
        print("+" * 20 )
        func(*x , ** y)
        print("+" * 20 )
    return inner
def star(func):
    def inner(*x,**y):
        print("*" * 20 )
        func(*x , ** y)
        print("*" * 20 )
    return inner
@plus
@dash
@star
def msg(name):
    print("I am " + name)

msg("MAJID")