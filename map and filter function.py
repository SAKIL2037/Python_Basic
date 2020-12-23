def sqare(x):
    return x*x

num = [1,2,3,4,5]

result = list(map(sqare,num))

print(result)


rslt = list(filter(lambda x: x%2!=0,num))
print(rslt)

