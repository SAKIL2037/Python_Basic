#AND operator

num1 = 20
num2 = 50
num3 = 40

if num1> num2 and num1 >num2:
    print(num1)
elif num2>num1 and num2 >num3:
    print(num2)
else:
    print(num3)

#OR operator


ch = 'b'

if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
    print("vowel")
else:
    print('consonant')

#NOT operator

num = 2

if not num != 20:
    print(" equal")
else:
    print("not equal")