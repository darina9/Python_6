
a = [1,1,1,3,3,8,4,4,5,5,2,2,9]

b = list(filter(lambda x: a.count(x)==1, a))

print(f"список неповторяющихся элементов: {b}")