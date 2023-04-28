#enter a number that has Extand zero on 2 and 5
# x = int(input("enter a number: "))
# if x % 2 == 0 and x % 5 == 0:
#     print("True")
# else:
#     print("false")
# ------------------------
# give The triangle's sides And check which kind of triangle is here
x = int(input("enter a number1: "))
y = int(input("enter a number2: "))
z = int(input("enter a number3: "))
if x < y + z and y < x + z and z<y+x :
        print("mitavand mosalas bashad")
if x == y and y == z:
        print("motasavyol azla")
if x == y or x == z or y == z:
        print("motasavyol saghain")
if (x**2 + y**2 ) == z**2 or (x**2 + z**2 ) == y**2 or (z**2 + y**2 ) == x**2 :
    print("ghaemolzaview")
if x != y and y != z and x!=z:
       print("mokhtalef")     
else:
     print("nemitavanda")    


