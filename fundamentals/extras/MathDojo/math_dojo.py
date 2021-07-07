class MathDojo:
    def __init__(self):
        self.result = 0
    #user can add with positive int and subtract with negative. add_or_subtract(1,-3,4,5,-6)... etc
    def add_or_subtract(self, *nums):
        for x in nums:
            self.result += x
        return self
    def multiply(self, *nums):
        for x in nums:
            self.result = self.result * x
        return self
    def divide(self, *nums):
        for x in nums:
            self.result = self.result / x
        return self
    def clear_calculator(self):
        self.result = 0
        return self

calculator = MathDojo()
x = calculator.add_or_subtract(2,-1,4,6).multiply(3,4).divide(4,2).result
print(x)