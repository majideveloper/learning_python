# first way
def max3(a,b,c):
    return max(a,b,c)
x=int(input("x:"))
y=int(input("y:"))
z=int(input("z:"))
print("max",max3(x,y,z))
# second way
def max3():
    x = int(input("x:"))
    y = int(input("y:"))
    z = int(input("z:")) 
    return max(x,y,z)

print("max",max3())