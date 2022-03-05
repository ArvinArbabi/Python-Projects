#We have two monkeys, a and b,
#and the parameters a_smile and b_smile indicate if each is smiling. 
#We are in trouble if they are both smiling or if neither of them is smiling. 
#Return True if we are in trouble.

from operator import truediv


def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    if not a_smile and not b_smile:
        return True
    return False

# print(monkey_trouble(True, True))
# print(monkey_trouble(False, False))
# print(monkey_trouble(False, True))
# print(monkey_trouble(True, False))

#Given two int values, return their sum.
#Unless the two values are the same, then return double their sum.

def sum_double(a, b):
    if a == b:
        return (a + b) * 2
    else:
        return a + b

# print(sum_double(1,2))
# print(sum_double(0,0))
# print(sum_double(1,9))
# print(sum_double(8,8))

#Given an int n, return the absolute difference between n and 21, 
#except return double the absolute difference if n is over 21.

def diff21(n):
    if n > 21:
        return (n - 21) * 2
    else:
        return 21 - n

# print(diff21(19))
# print(diff21(100))
# print(diff21(10))
# print(diff21(21))

# We have a loud talking parrot. 
# The "hour" parameter is the current hour time in the range 0..23.
# We are in trouble if the parrot is talking and the hour is before 7 or after 20. 
# Return True if we are in trouble.

def parrot_trouble(hour, talking):
    return (talking and (hour < 7 or hour > 20))
    # if not talking:
    #     return False
    # if hour < 7 or hour > 20:
    #     return True
    # return False

# print(parrot_trouble(6,True))
# print(parrot_trouble(6,False))
# print(parrot_trouble(7,True))
# print(parrot_trouble(21,True))
# print(parrot_trouble(8,True))

# Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
def makes10(a, b):
    return a + b == 10 or a == 10 or b == 10

print(makes10(9,10))
print(makes10(9,1))
print(makes10(10,10))
print(makes10(10,7))


    