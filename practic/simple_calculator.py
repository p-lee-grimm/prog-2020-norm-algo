class Calculator:
    def __init__(self, init_value=0):
        self.value = init_value

    def add(self, *args):
        self.value += sum(args)
        return self

    def multiply(self, *args):
        for x in args:
            self.value *= x
        return self

    def divide(self, *args, integer_divide=False):
        for x in args:
            if integer_divide:
                self.value //= x
            else:
                self.value /= x
        return self

    def subtract(self, *args):
        self.value -= sum(args)
        return self

    def __repr__(self):
        return self.value

    def __str__(self):
        return str(self.value)


if __name__ == '__main__':
    calculator = Calculator(100)
    print(calculator)
    print(calculator.add(1, 2, 3, 5.1).multiply(4, 0.123).subtract(4, 1, -100).divide(5, integer_divide=True))
    print(Calculator(100) + 10)
    print(10 + Calculator(12))
    print(Calculator(123) - Calculator(14))
    print(Calculator(14) / Calculator(2))
