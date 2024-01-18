# Chukwueemka Nwachukwu
# W211379501
# Cosc - Intro to Python 2
# Operator Overloading

from math import gcd


class Rational:
    def __init__(self, top, bot):
        # Cant divide by 0, obvs so
        if bot == 0:
            raise ValueError("bottom cannot be zero")
        # Gotta simplify that fraction
        cd = gcd(top, bot)
        self._num = top // cd
        self._den = bot // cd

    def __eq__(self, other):
        # makin sure if theyre equal
        match other:
            case Rational():
                # If its a fraction, compare num and den
                return self._num == other._num and self._den == other._den
            case int():
                # If its an int, turn it into a fraction first
                return self._num == other * self._den
            case float():
                # If its a float, turn self into a float first
                return float(self) == other
            case _:
                # If its something else just return default behavior
                return NotImplemented

    def __lt__(self, other):
        # Checkin if self is less than other
        match other:
            case Rational():
                # Cross-multiply and compare
                return self._num * other._den < other._num * self._den
            case int():
                # Turn the int into a fraction first
                return self._num < other * self._den
            case float():
                # Turn self into a float first
                return float(self) < other
            case _:
                # If its something else just return default behavior
                return NotImplemented

    def __le__(self, other):
        # check if self is less than or equal to other
        match other:
            case Rational():
                return self._num * other._den <= other._num * self._den
            case int():
                return self._num <= other * self._den
            case float():
                return float(self) <= other
            case _:
                return NotImplemented

    def __gt__(self, other):
        # Checkin if self is greater than other
        match other:
            case Rational():
                return self._num * other._den > other._num * self._den
            case int():
                return self._num > other * self._den
            case float():
                return float(self) > other
            case _:
                return NotImplemented

    def __ge__(self, other):
     # Checkin if self is greater than or equal to other
        match other:
            case Rational():
                return self._num * other._den >= other._num * self._den
            case int():
                return self._num >= other * self._den
            case float():
                return float(self) >= other
            case _:
                return NotImplemented

    def __add__(self, other):
        # Addin self and other
        match other:
            case Rational():
                # If other is a fraction, cross-multiply and add
                top = (self._num * other._den) + (other._num * self._den)
                bot = self._den * other._den
                return Rational(top, bot)
            case int():
                top = (self._num) + (other * self._den)
                bot = self._den
                return Rational(top, bot)
            case float():
                return float(self) + other
            case _:
                return NotImplemented

    def __sub__(self, other):
        # Subtractin other from self
        match other:
            case Rational():
                top = (self._num * other._den) - (other._num * self._den)
                bot = self._den * other._den
                return Rational(top, bot)
            case int():
                top = (self. _num) - (other * self. _den)
                bot = self. _den
                return Rational(top, bot)
            case float():
                return float(self)-other
            case _:
                return NotImplemented

    def __truediv__(self, other):
        # Dividin self by other
        match other:
            case Rational():
                top = self._num * other._den
                bot = self._den * other._num
                return Rational(top, bot)
            case int():
                top = self._num
                bot = self._den * other
                return Rational(top, bot)
            case float():
                if not 0 == other:
                    return float(self) / other
                else:
                    # exception if the value of other is 0
                    raise ZeroDivisionError("cant divide by zero")
            case _:
                return NotImplemented

    def __mul__(self, other):
        # Multiplin self and other
        match other:
            case Rational():
                # If other is a fraction, multiply num and den separately
                top = self._num * other._num
                bot = self._den * other._den
                return Rational(top, bot)
            case int():
                top = self._num * other
                bot = self._den
                return Rational(top, bot)
            case float():
                return float(self) * other
            case _:
                return NotImplemented

    def __abs__(self):
        # the absolute value of self
        top = abs(self._num)
        bot = abs(self._den)
        return Rational(top, bot)

    def __pow__(self, power):
        # Raising self to the power of power
        if not isinstance(power, int):
            # exception since power gotta be an int
            raise TypeError("Power must be an integer")
        if power >= 0:
            # If power is non-negative, raise num and den to the power separately
            return Rational(self._num ** power, self._den ** power)
        else:
            return Rational(self._den ** -power, self._num ** -power)

    def __float__(self):
        # Turnin self into a float
        return self. _num/self. _den

    def __str__(self):
        # Gettin a string representation of self
        return f"{self._num}/{self._den}"


if __name__ == "__main__":
    p = Rational(2, 3)
    q = Rational(-5, 7)
    print(p + q)  # -1 / 21
    print(p - q)  # 29 / 21
    print(p * q)  # -10 / 21
    print(p / q)  # -14 / 15
    print(p + q)  # -1 / 21
    print(p + 2)  # 8 / 3
    result = (p + 1.5)
    print(f"{result:.2f}")  # 5 / 3 (fixed floating point issue)
    print(p * 1.5)  # 1
    result = (p / 1.5)
    print(f"{result:.2f}")  # 4 / 9 (fixed floating point issue)
    print(abs(q))  # 5 / 7
    print(p ** 2)  # 4 / 9
    print(q ** -2)  # 49 / 25
    print(p < q)  # False
    print(p <= q)  # False
    print(p == q)  # False
    print(p > q)  # True
    print(p >= q)  # True
    print(p != q)  # True
    print(p > 2)  # False
    print(p <= p)  # True
    print(p > 0.5)  # True
