# try:
#     x = 10 / 0
# except:
#     print("that is not possible")

class Calculator:
    def add(self, x, y):
        return x + y
    
    def minus(self, x, y):
        return x - y
    
    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        try:
            return x / y
        except ZeroDivisionError as e:
            print("you cannot divide by zero")
        except TypeError as e:
            print("you didnt input a valid number")
            print(e)


calc = Calculator()
print(calc.add(4, 5))
print(calc.minus(4, 5))
print(calc.multiply(4, 5))
print(calc.divide(4, 0))

print(calc.divide("reza", "arvin"))