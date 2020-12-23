#xargs tuple

def add(*number):
    sum=0
    for num in number:
        sum = sum + num

    print(sum)

add(1,2)
add(1,2,3,4)

#xxargs Dictionari

def student(**info):
    print(info)


student(id = 101,name = "sakil")
