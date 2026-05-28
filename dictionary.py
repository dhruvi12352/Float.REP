
d = {"name": "Dhruvi", "age": 20}

print(d)




d = {"name": "Dhruvi", "age": 20}

print(d["name"])



d = {"name": "Dhruvi"}

print(d.get("name"))
print(d.get("age"))




d = {"name": "Dhruvi"}

d["age"] = 20

print(d)




d = {"age": 20}

d["age"] = 21

print(d)


d = {"a": 1, "b": 2}

print(d.keys())


d = {"a": 1, "b": 2}

print(d.values())


d = {"a": 1, "b": 2}

print(d.items())


d = {"name": "Dhruvi"}

d.setdefault("age", 20)

print(d)

d = {"a": 1}

d.update({"b": 2})

print(d)


d = {"a": 1, "b": 2}

value = d.pop("a")

print(value)
print(d)


d = {"a": 1, "b": 2}

item = d.popitem()

print(item)
print(d)


d = {"a": 1, "b": 2}

d.clear()

print(d)


d1 = {"a": 1}

d2 = d1.copy()

print(d2)


keys = ["a", "b", "c"]

d = dict.fromkeys(keys, 0)

print(d)


d = {"name": "Dhruvi"}

print("name" in d)


d = {"a": 1, "b": 2, "c": 3}

print(len(d))


d = {"c": 3, "a": 1, "b": 2}

print(sorted(d))


keys = ["name", "age"]
values = ["Dhruvi", 20]

d = dict(zip(keys, values))

print(d)


d = {"a": 1, "b": 0}

print(any(d))


d = {"a": 1, "b": 2}

print(all(d))


d = {x: x * x for x in range(5)}

print(d)


student = {
    "name": "Dhruvi",
    "marks": {
        "math": 90,
        "python": 95
    }
}

print(student["marks"]["python"])


d1 = {"a": 1}
d2 = {"b": 2}

merged = {**d1, **d2}

print(merged)


d1 = {"a": 1}
d2 = {"b": 2}

print(d1 | d2)


d = {"a": 1, "b": 2}

for key, value in d.items():
    print(key, value)
