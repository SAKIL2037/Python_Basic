
temp = input("Enter the value: ")

list = temp.split()

print(list)
sum = 0
for x in list:
    sum = sum + int(x)

print(sum)


numberOfWord = 0
numberOfLetter = 0
numberOfDigite = 0

n = input("Enter the value: ")

for x in n:
    x = x.lower()
    if x >='a' and x <= 'z':
        numberOfLetter = numberOfLetter + 1
    elif x >= '0' and x <='9':
        numberOfDigite = numberOfDigite + 1
    elif x == ' ':
        numberOfWord = numberOfWord + 1


print("Total Word = ",numberOfWord+1)
print("Total letter = ",numberOfLetter)
print("Total digite = ",numberOfDigite)