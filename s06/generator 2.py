from time import perf_counter
def list_generator(start , end , step=1):
    new_range=[]
    while start < end :
        new_range.append(start)
        start += step
    return new_range


def gen_range(start , end , step=1):
    while start < end :
        yield start
        start += step


start = perf_counter()
gr = gen_range(1,500000000)
s = 0
for i in gr :
    if i == 3:
        break
    s+= i**2
end = perf_counter()
print("gr time is:",end-start)
start2 = perf_counter()
lr = list_generator(1,500000000)
s = 0
for i in gr :
    if i == 3:
        break
    s+= i**2
end2 = perf_counter()
print("gr time is:",end2-start2)

