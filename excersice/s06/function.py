# # -------------------1
# # len()
# def len2(it):
#     counter = 0
#     for _ in it :
#         counter += 1
#     return counter
# s="saafasfasfasf"
# l=[5,87465,21,3,8,98,6354]
# t=("a", "b" ,"c","d")
# print(len2(s))
# print(len2(l))
# print(len2(t))
# 2---------------------
# def max2(*args):
#     m=args[0]
#     for i in args:
#         if i > m:
#             m=i
#     return m
# print(max2(1,54,654,654,87,7987,322,231,-500))
# -------------------3
# def square(n):
#     for i in range(1 , n):
#         if i ** 2 == n:
#             print(f"Yes! {i} * {i} = {n} ")
#             break
#     else:
#         print("No!- ")
#
# numberr = int(input("Enter a Number: "))
# square(numberr)
# ----------------4------------------
def discount(rate,price):
    discount_rate = int(price * rate /100)
    new_price = int(price -discount_rate)
    print("discount rate: ",discount_rate)
    print("New Price is:",new_price)

rate = int(input("Rate; "))
price = int(input("price"))
discount(rate,price)