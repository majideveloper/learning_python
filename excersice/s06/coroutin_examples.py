def cen_gen(words):
    print("Hello")
    w = None
    while True:
        word = yield w
        if word not in words:
            w = word
        else:
            w = "*" * len(word)

g = cen_gen(["khar","gav","loos",])
next(g)
print(g.send("khar"))
print(g.send("majid"))
print(g.send("gav"))
print(g.send("ali"))
print(g.send("sani"))
print(g.send("loos"))
print(g.send("mashin"))