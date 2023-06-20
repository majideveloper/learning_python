def descending(mylist):
    print(sorted(mylist))


def ascending(mylist):
    print(sorted(mylist, reverse=True))


def mysort(f, mylist):
    f(mylist)


mysort(ascending, [1, 8, 3, 541, 3484, 654, 132, 8813, 779])
