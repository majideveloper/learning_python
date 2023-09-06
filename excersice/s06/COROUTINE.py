from functools import wraps
def coroutine(func):
    @wraps(func)
    def start(*args,**kwargs):
        gn = func()
        next(gn)
        return gn
    return start
@coroutine
def my_gen():
    print("Star!!")
    for i in range(10):
        name = yield i
        print("My name is :" , name)

g = my_gen()
# print(next(g))
print(g.send("majid"))
print(g.send("ali"))