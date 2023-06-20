def repeat(number,digit):
    count=0
    while number > 0:
        if number % 10 == digit:
            count += 1
        number = number // 10

    return count
number = float(input("number:"))
digit = float(input("digit:"))
print(digit,"Repeat",repeat(number,digit),"times")