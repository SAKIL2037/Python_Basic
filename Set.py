num1 = {1,2,3,4,5}

print(num1)
num1.add(6)
print(num1)
num1.remove(6)
print(num1)

temp = [4,5,6,7,8]
print(temp)

num2 = set(temp)

print(6 in num1)
print(6 in num2)

print(num1 | num2)
print(num1 & num2)
print(num1 - num2)