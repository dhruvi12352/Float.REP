
x = 10
y = -25

print(x)
print(y)


x = 0b1010

print(x)


x = 0o12

print(x)


x = 0xA

print(x)


print(int("42"))



print(int(3.9))



print(int(True))




x = 10

print(x.bit_length())


x = 7

print(x.bit_count())




x = 65

result = x.to_bytes(1, byteorder="big")

print(result)


b = b'A'

result = int.from_bytes(b, byteorder="big")

print(result)




x = 10

print(x.as_integer_ratio())


x = -20

print(abs(x))


print(pow(2, 3))


print(divmod(10, 3))



x = 10

print(bin(x))


x = 10

print(oct(x))


x = 10

print(hex(x))


a = 10
b = 3

print(a + b)   
print(a - b) 
print(a * b)   
print(a // b)  
print(a % b)   
print(a ** b)  


a = 10
b = 20

print(a > b)
print(a < b)
print(a == b)


a = 5
b = 3

print(a & b)   
print(a | b)   
print(a ^ b)  
print(~a)      
print(a << 1)  
print(a >> 1)  




x = 999999999999999999999999999

print(x)

