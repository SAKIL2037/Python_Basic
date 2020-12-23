try:
    list = [20,0,30]
    result = 20/list[2]
    print(result)
    print("Done")
except ZeroDivisionError:
    print("Dividing by Zero is not possible")
except IndexError:
    print("list index out of range")
finally:
    print("Succesfully")



try:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 2nd number: "))
    result = num1 / num2
    print(result)
except (ValueError,ZeroDivisionError):
    print("You have entered incorrect input")
finally:
    print("Thanks")


def voter(age):
    if(age<18):
        raise ValueError("Invalid Voter")
    return "yor are allowed to vote"

try:
    print(voter(18))
except ValueError as e:
    print(e)

