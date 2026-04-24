import math

class AreaCalc:
    def calculate(self, length: int, width: int = None) -> float:
        if width is None:
            result = math.pi * length **2
            return round(result, 2)
        return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))