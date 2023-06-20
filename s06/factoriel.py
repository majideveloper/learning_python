def fact(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f
def sum_fact(n):
    sumf = 0
    for i in range(1 , n+1):
        sumf += fact(i)
    return sumf
number = int(input("enter a number"))
print("Sum is :", sum_fact(number))

