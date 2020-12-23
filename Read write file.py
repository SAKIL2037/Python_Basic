file = open("sakildetails.txt","r")

print(file.readable())
print(file.writable())
text = file.read()
print(text)
file.close()

file = open("sakildetails.txt","r+")

print(file.readable())
print(file.writable())
textfile = file.readlines()
print(textfile)
file.close()


file = open("sakildetails.txt","r+")

print(file.readable())
print(file.writable())
for text in file:
    print(text)
file.close()


file = open("sakildetails.txt","r+")

size = len(file.read())
print(size)
file.close()


file = open("sakildetails.txt","a")

file.write("\n jolil - job holder")
file.close()
