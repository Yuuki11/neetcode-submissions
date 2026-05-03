import math

class AreaCalc:
    @classmethod
    def calculate(cls, length: int, width: int = None) -> float:
        if width is None:
            result = math.pi * length **2
            return round(result, 2)
        return length * width
    

    
# Don't modify the following code
calc = AreaCalc()
print(AreaCalc.calculate(5))    
print(calc.calculate(4, 6))