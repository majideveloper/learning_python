# def func(x):
#     yield x ** 2
#     print("majid")
#     print("hello")
#     print("hello")
#     yield x ** 3
#     print("hello")
#     yield x ** 3
#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")
#     print("hello")
#
# x = func(5)
# print(next(x))
# print(next(x))
# print(next(x))
def generator_():
    print("Welcome!!!")
    for i in range(500):
        yield i ** 2


g = generator_()
for i in g:
    print(i)
