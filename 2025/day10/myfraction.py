
import math
class MyFraction:
    def __init__(self, frac):
        self.num = frac.num
        self.den = frac.den

    def __init__(self, num: int, den: int):
        self.num = num
        self.den = den

        self.simplify()

    def simplify(self):
        g = math.gcd(self.num, self.den)

        self.num = self.num // g
        self.den = self.den // g

        if self.den < 0:
            self.num *= -1
            self.den *= -1

    def inv(self):
        self.num, self.den = self.den, self.num

    def __mul__(self, value):
        if type(value) is MyFraction:
            return MyFraction(
                self.num * value.num,
                self.den * value.den
            )
        
        if type(value) is int:
            return MyFraction(
                self.num * value,
                self.den
            )
        
        assert False, f"Fraction * {type(value)} not implemented"
    
    def __truediv__(self, value):
        if type(value) is MyFraction:
            assert value.num != 0, "division by fractional 0"

            return MyFraction(
                self.num * value.den,
                self.den * value.num
            )
        
        if type(value) is int:
            assert value != 0, "division by integer 0"

            return MyFraction(
                self.num,
                self.den * value
            )
        
        assert False, f"Fraction / {type(value)} not implemented"
    
    def __add__(self, value):
        if type(value) is MyFraction:
            return MyFraction(
                self.num * value.den + value.num * self.den,
                self.den * value.den
            )
        
        if type(value) is int:
            return MyFraction(
                self.num + value * self.den,
                self.den
            )
        
        assert False, f"Fraction + {type(value)} not implemented"

    def __sub__(self, value):
        if type(value) is MyFraction:
            return MyFraction(
                self.num * value.den - value.num * self.den,
                self.den * value.den
            )
        
        if type(value) is int:
            return MyFraction(
                self.num - value * self.den,
                self.den
            )
        
        assert False, f"Fraction + {type(value)} not implemented"
    
    def __str__(self):
        if self.den == 1:
            return f"{self.num}"
        
        return f"{self.num}/{self.den}"
    
    def __eq__(self, value):
        assert math.gcd(self.num, self.den) == 1, "fraction not simplified (how did this happen?)"

        if type(value) is MyFraction:
            return self.num == value.num and self.den == value.den
        
        if type(value) is int:
            if self.den != 1:
                return False
            
            return self.num == value
    
        assert False, f"Fraction == {type(value)} not implemented"


def main():
    print(MyFraction(1,1))
    print(MyFraction(1,1) / 2)
    print(MyFraction(1,1) * 2)
    print(MyFraction(2,3) * MyFraction(1,3) * MyFraction(3,1))
    print(MyFraction(1,1) == 1)

if __name__ == "__main__":
    main()