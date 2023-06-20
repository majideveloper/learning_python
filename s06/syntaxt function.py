# first way
def cube(x):
    return x ** 3
n = int(input("enter x:"))
y=cube(n)
print(y)
# ------
# secound way
def cube2():
    x = int(input("enter x:"))
    return x ** 3
n=cube2()
print(n)
# third way
def cube3():
    x = int(input("enter x:"))
    print(x ** 3)
cube3() 