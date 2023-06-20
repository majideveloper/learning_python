from random import random,choice,uniform,randint,seed,randrange,shuffle
# # print(random())
# # # seed(213)
# # print(random())
# # for _ in range(10):
# #     print(5-(random()*(10-5)))
# # print("**********")
# # for _ in range(10):
# #     print(uniform(5,10))
# #
# # print("**********")
# # for _ in range(10):
# #     print(randint(5,10))
#
# # for _ in range(10):
# #     print(randrange(5,100,2))
# tas = {1:0 , 2:0 , 3:0 ,4:0, 5:0,6:0}
# for _ in range(20):
#     tas[randint(1,6)]+=1
#     print(tas)
# x=[1,2,31,3213,234,234,4541,5459]
# y=x.copy()
# shuffle(y)
# print(y)

# min_=min(x,y)
# max_=max(x,y)
# for i in range(min_ , max_ +1):
#
#     print(i)
x=int(input("enter a number"))
y=int(input("enter a number"))
for i in range(1,x+1):
    if(x%i==0 and y%i==0):
        print(i,end="\t")

