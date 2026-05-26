
lst = [1, 2]
lst.append(3)
print(lst)   



lst = [1, 2]
lst.extend([3, 4])
print(lst)   



lst = [1, 3]
lst.insert(1, 2)
print(lst)   



lst = [1, 2, 3]
lst.remove(2)
print(lst)   



lst = [10, 20, 30]
value = lst.pop()
print(value)   

print(lst)     



lst = [10, 20, 30]
value = lst.pop(1)
print(value)   

print(lst)     



lst = [1, 2, 3]
lst.clear()
print(lst)   



lst = [10, 20, 30]
print(lst.index(20))   



lst = [1, 1, 2, 3]
print(lst.count(1))   



lst = [3, 1, 2]
lst.sort()
print(lst)   



lst = [3, 1, 2]
lst.sort(reverse=True)
print(lst)   



lst = [1, 2, 3]
lst.reverse()
print(lst)   



lst1 = [1, 2, 3]
lst2 = lst1.copy()
print(lst2)   



lst = [1, 2, 3, 4]
print(len(lst))   



lst = [5, 2, 8]
print(min(lst))   



lst = [5, 2, 8]
print(max(lst))   


lst = [1, 2, 3]
print(sum(lst))   



lst1 = [1, 2]
lst2 = [3, 4]
print(lst1 + lst2)   

lst = [0]
print(lst * 5)   



lst = [1, 2, 3]
print(2 in lst)   

lst = [1, 2, 3, 4, 5]
print(lst[1:4])   



lst = ["a", "b", "c"]

for index, value in enumerate(lst):
    print(index, value)


lst1 = [1, 2, 3]
lst2 = ["a", "b", "c"]

print(list(zip(lst1, lst2)))




lst = [0, False, 5]
print(any(lst))   



lst = [1, True, 5]
print(all(lst))   
# True


lst = [1, 2, 3]

result = list(map(lambda x: x * 2, lst))
print(result)


lst = [1, 2, 3, 4]

result = list(filter(lambda x: x % 2 == 0, lst))
print(result)


lst = [x * 2 for x in range(5)]
print(lst)

