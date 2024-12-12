#Задание 1

class Calc:
    def plus(self, a, b):
        return a + b

    def minus(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error"
        else:
            return a / b

calc = Calc()
a = 5
b = 7

print(f"{calc.plus(a, b)}\n{calc.minus(a, b)}\n{calc.multiply(a, b)}\n{calc.divide(a, b)}")