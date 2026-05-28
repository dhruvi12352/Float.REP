# Creating a dictionary
d = {"name": "Dhruvi", "age": 20}

print(d)

# {'name': 'Dhruvi', 'age': 20}

# Accessing values
d = {"name": "Dhruvi", "age": 20}

print(d["name"])

# Dhruvi

# get()
d = {"name": "Dhruvi"}

print(d.get("name"))
print(d.get("age"))

# Dhruvi
# None

# Adding new key-value pair
d = {"name": "Dhruvi"}

d["age"] = 20

print(d)

# {'name': 'Dhruvi', 'age': 20}

# Updating value
d = {"age": 20}

d["age"] = 21

print(d)

# {'age': 21}

# keys()
d = {"a": 1, "b": 2}

print(d.keys())

# dict_keys(['a', 'b'])

# values()
d = {"a": 1, "b": 2}

print(d.values())

# dict_values([1, 2])

# items()
d = {"a": 1, "b": 2}

print(d.items())

# dict_items([('a', 1), ('b', 2)])

# setdefault()
d = {"name": "Dhruvi"}

d.setdefault("age", 20)

print(d)

# {'name': 'Dhruvi', 'age': 20}

# update()
d = {"a": 1}

d.update({"b": 2})

print(d)

# {'a': 1, 'b': 2}

# pop()
d = {"a": 1, "b": 2}

value = d.pop("a")

print(value)
print(d)

# 1
# {'b': 2}

# popitem()
d = {"a": 1, "b": 2}

item = d.popitem()

print(item)
print(d)

# Removes last inserted item

# clear()
d = {"a": 1, "b": 2}

d.clear()

print(d)

# {}

# copy()
d1 = {"a": 1}

d2 = d1.copy()

print(d2)

# {'a': 1}

# fromkeys()
keys = ["a", "b", "c"]

d = dict.fromkeys(keys, 0)

print(d)

# {'a': 0, 'b': 0, 'c': 0}

# Checking key existence
d = {"name": "Dhruvi"}

print("name" in d)

# True

# len()
d = {"a": 1, "b": 2, "c": 3}

print(len(d))

# 3

# sorted()
d = {"c": 3, "a": 1, "b": 2}

print(sorted(d))

# ['a', 'b', 'c']

# dict using zip()
keys = ["name", "age"]
values = ["Dhruvi", 20]

d = dict(zip(keys, values))

print(d)

# {'name': 'Dhruvi', 'age': 20}

# any()
d = {"a": 1, "b": 0}

print(any(d))

# True

# all()
d = {"a": 1, "b": 2}

print(all(d))

# True

# Dictionary comprehension
d = {x: x * x for x in range(5)}

print(d)

# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Nested dictionary
student = {
    "name": "Dhruvi",
    "marks": {
        "math": 90,
        "python": 95
    }
}

print(student["marks"]["python"])

# 95

# Merging dictionaries
d1 = {"a": 1}
d2 = {"b": 2}

merged = {**d1, **d2}

print(merged)

# {'a': 1, 'b': 2}

# Dictionary merge operator (Python 3.9+)
d1 = {"a": 1}
d2 = {"b": 2}

print(d1 | d2)

# {'a': 1, 'b': 2}

# Iterating through dictionary
d = {"a": 1, "b": 2}

for key, value in d.items():
    print(key, value)

# a 1
# b 2