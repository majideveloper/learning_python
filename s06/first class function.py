def descending(mylist):
    print(sorted(mylist))


def ascending(mylist):
    print(sorted(mylist, reverse=True))


def mysort(f, mylist):
    f(mylist)

while True:

    choice=input("Which Sort do you want to do?\n\t1)descending\n\t2)descending\nEnter your choice:")
    l1 = [input("enter your numbers").split(",")]
    if choice == "1":

        mysort(descending, l1)
    elif choice == "2":
        mysort(ascending,>> l1)
        break
    else:
        print("Invalid input")






