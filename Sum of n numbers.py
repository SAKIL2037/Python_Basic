#2+4+6............+n

n = int(input("Enter the value of N :" ))

i = 2
sum = 0

while i<=n:
    sum = sum+i
    print(i)
    i=i+2

print("Sum = ",sum)
