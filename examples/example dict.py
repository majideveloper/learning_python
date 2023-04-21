# make a real dictionary
# dictionary = {}
# key = input("enter a word : ")
# mean1 = input("enter a mean1 : ")
# mean2 = input("enter a mean2 : ")
# mean3 = input("enter a mean3 : ")
# mean4 = input("enter a mean4 : ")
# dictionary[key] = [mean1,mean2,mean3,mean4]
# print(dictionary)
# ----------------?
dictionary = {}
key = input("enter a word : ")
meanings= input("enter a means : ").split(",")
dictionary[key] = meanings
print(dictionary)