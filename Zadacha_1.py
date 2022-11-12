a = [1.1, 1.2, 3.1, 5, 10.01]

a = list(i for i in map(lambda x : x%1, a) if i != 0)

print (f'разница равна: {max(a)-min(a)}')