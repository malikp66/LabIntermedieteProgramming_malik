from fractions import Fraction as PyFraction

class Fraction:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        self.numerator = numerator
        self.denominator = denominator
        self._simplify()

    def _simplify(self):
        fraction = PyFraction(self.numerator, self.denominator)
        self.numerator = fraction.numerator
        self.denominator = fraction.denominator

    def to_rational(self):
        return f"{self.numerator}/{self.denominator}"

    def to_float(self):
        return self.numerator / self.denominator

# Example usage
fraction = Fraction(2,6)
print(fraction.to_rational())  
print(fraction.to_float())
