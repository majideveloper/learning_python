#enter a number and print each number
x = int(input("Enter x: "))
temp = x % 10
print(temp)
x = x // 10
temp = x % 10
print(temp)
x = x // 10
print(x)
