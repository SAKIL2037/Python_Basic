from collections import deque
#FIFO
bank = deque(["sakil","anis","bijoy"])

print(bank)
print("Now the first people is : ",bank[0])
bank.popleft()
if not  bank:
    print("No People left")
else:
    print("Now the first people is : ",bank[0])

bank.popleft()
if not  bank:
    print("No People left")
else:
    print("Now the first people is : ",bank[0])

bank.popleft()
if not  bank:
    print("No People left")
else:
    print("Now the first people is : ",bank[0])

