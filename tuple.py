
tup = (1, 2, 3)
print(tup)


tup = (10,)
print(type(tup))


coordinates = 10, 20
print(coordinates)


x, y = (10, 20)
print(x)
print(y)


first, *rest = (1, 2, 3, 4)
print(first)
print(rest)


tup = (1, 1, 2, 3)
print(tup.count(1))




tup = (10, 20, 30)
print(tup.index(20))




tup = (1, 2, 3, 4)
print(len(tup))




tup = (5, 2, 8)
print(min(tup))




tup = (5, 2, 8)
print(max(tup))



tup = (1, 2, 3)
print(sum(tup))



tup1 = (1, 2)
tup2 = (3, 4)






tup = (0,)
print(tup * 3)




tup = (1, 2, 3)

print(2 in tup)



tup = ("a", "b", "c")

print(tup[0])
print(tup[-1])


tup = (1, 2, 3, 4, 5)

print(tup[1:4])


tup = ((1, 2), (3, 4))

print(tup[0])
print(tup[1][0])


tup = ("a", "b", "c")

for index, value in enumerate(tup):
    print(index, value)

tup1 = (1, 2, 3)
tup2 = ("a", "b", "c")

print(tuple(zip(tup1, tup2)))


tup = (0, False, 5)

print(any(tup))


tup = (1, True, 5)

print(all(tup))


lst = [1, 2, 3]

print(tuple(lst))
