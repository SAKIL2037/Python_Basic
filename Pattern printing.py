'''
*
**
***
****
*****
'''
n = int(input("Enter the value of n: "))
for i in range(n+1):
    print(i*"*")

'''
*
***
*****
*******
'''

n = int(input("Enter the value of n: "))
for i in range(1,n+2,2):
    print(i*"*")
'''
    *
   **
  ***
 ****
*****
'''
n = int(input("Enter the value of n: "))
temp = n
for i in range(n+1):
    print(temp*" "+i*"*")
    temp= temp - 1