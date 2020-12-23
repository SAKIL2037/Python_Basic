subject = ["C","C++","Java","Python","PHP","OS"]

print(subject)
print(subject[0])
print(subject[1:3])
print(subject[2:])
print(subject[:3])
print(subject[:-1])
print(subject + ["Android"])

print(len(subject))
subject.append("Basic")
print(subject)

subject.insert(2,30)
print(subject)

subject.remove(30)
print(subject)

subject.sort()
print(subject)

number = [5,4,8,9,2,1,6,2,2]

number.sort()
print(number)

number.reverse()
print(number)

number.pop()
print(number)

number2 = number.copy()
print(number2)

print(number.index(9))

print(number.count(2))

number.clear()


