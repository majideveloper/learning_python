import random
import string
lower = string.ascii_lowercase
upper = string.ascii_uppercase
symbols= "!#@$%^&*()_+:?><}|"
numbers = "123456789"
all =lower+upper+symbols+numbers

while True :
    print("Enter your choice:\t\n 1)Create Password: \t\n 2)exit")
    choice = input("Enter your choice")
    if choice == "1" :
        length = int(input("enter the lenght Of your Password:"))
        password = "".join(random.sample(all,length))
        print(password)
    elif choice == "2":
        break
    else:
        print("Wrong number")
