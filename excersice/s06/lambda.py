# ------1-------------
# lst = [45,564,12,8,11,23,12,322,98]
# print("len list: ", len(lst))
# odd = len(list(filter(lambda x : x%2 !=0 ,lst)))
# print("len odd: ", odd)
# even = len(list(filter(lambda x : x%2 == 0 , lst)))
# print("len even",even)
# ------------2------------
# lst = [("majid",20),("ali",520),("reza",12),("mammad",64)]
# lst.sort(key=lambda x : x[1])
# print(lst)
# -----------------
lst = [1,3,5,12,887,32,6,8,9]
square = list((map(lambda x : x**2 ,lst )))
print(square)