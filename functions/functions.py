from unittest import result


def func1():
    print("hello my name is arvin")

func1()
#directly calling function
print(func1())
#function is also being called...
#in the print statment... 
#since function doesnt provide a result python returns it as none
print(func1)
#shows address in RAM

def func2(arg1, arg2):
    print(arg1, " ", arg2)

def cube(x):
    return x * x * x


func2(10, 20)
print(func2)

print(cube(8))

def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

print(power(2))
print(power(2,99))

def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

print(multi_add(4,5,10,10,4))