
text = "dhruvi"
print(text.upper())   


text = "DHRUVI"
print(text.lower()) 


text = "hello dhruvi"
print(text.title())   


text = "python"
print(text.capitalize())  


text = "PyThOn"
print(text.swapcase())  


text = "  hello  "
print(text.strip())  

#
text = "  hello"
print(text.lstrip())   


text = "hello   "
print(text.rstrip())  


text = "apple"
print(text.replace("a", "A"))  


text = "a,b,c"
print(text.split(","))  


text = "a,b,c"
print(text.rsplit(",", 1))   


text = "hello\nworld"
print(text.splitlines())  


words = ["hello", "world"]
print(" ".join(words))  


text = "python"
print(text.find("t"))  


text = "banana"
print(text.rfind("a"))  


text = "python"
print(text.index("t"))  


text = "banana"
print(text.rindex("a"))   


text = "banana"
print(text.count("a"))  


text = "python"
print(text.startswith("py"))  


text = "file.txt"
print(text.endswith(".txt")) 


text = "abc"
print(text.isalpha())   


text = "123"
print(text.isdigit())

text = "abc123"
print(text.isalnum())   


text = "   "
print(text.isspace())  


text = "HELLO"
print(text.isupper())  


text = "hello"
print(text.islower())   


text = "Hello World"
print(text.istitle())   


text = "123"
print(text.isnumeric())  


text = "123"
print(text.isdecimal())  


text = "python_var"
print(text.isidentifier())    


text = "hello"
print(text.isprintable())  


text = "python"
print(text.center(10, "-"))   


text = "python"
print(text.ljust(10, "-"))   


text = "python"
print(text.rjust(10, "-")) 


text = "42"
print(text.zfill(5)) 


text = "hello"
print(text.encode())   


text = "hello\tworld"
print(text.expandtabs(4))


name = "Dhruvi"
print("Hello {}".format(name)) 


data = {"name": "Dhruvi"}
print("Hello {name}".format_map(data))


table = str.maketrans("a", "A")
text = "apple"
print(text.translate(table))   


text = "hello-world"
print(text.partition("-"))   



text = "hello-world-python"
print(text.rpartition("-"))



text = "mrs.Dhruvi"
print(text.removeprefix("Mrs."))  


text = "notes.txt"
print(text.removesuffix(".txt"))  