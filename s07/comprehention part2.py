from random import randrange
def func():
    return randrange(50,150)
l1=[]
for i in range(20):
    x = func()
    if x  > 100:
         l1.append(x)
print(l1)
