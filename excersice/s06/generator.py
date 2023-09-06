# def my_enumerate(sequence, start = 0):
#     c = start
#     for i in sequence:
#         yield c,i
#         c += 1
#
# lst = ["majid","ali","reza"]
# for i,j in my_enumerate(lst):
#     print(i,j)
#
# # --------2-----------
# def fibonachi():
#     f1 = 0
#     yield f1
#     f2 = 1
#     yield f2
#     while True:
#         f3 = f1 +f2
#         yield f3
#         f1 = f2
#         f2 = f3
#
# fib = fibonachi()
# for _ in range(10):
#     print(next(fib))
# ----------4--------------
# def rev_str(s):
#     l = len(s)
#     for i in range(l-1 , -1 , -1):
#         yield s[i]
#
#
# rs=rev_str("majid  moradi")
# for ch in rs:
#     print(ch)
# ----------5--------------
# def my_gen(eve_or_odd = "e"):
#     c = 0
#     if eve_or_odd == "o":
#         c = 1
#     while True:
#         yield c
#         c+=2
#
# eo = my_gen("e")
# for i  in range(10):
#     print(next(eo))
# ----------6--------------
def num_gen():
    c = 1
    while True:
        s = ""
        for i in range(1 , c+1):
            s+= f"{c}\t"

        yield s
        c+=1

ng = num_gen()
for j in range(10):
    print(next(ng))