from app.calculator import Calculator


class TestCalculator:
    def test_add(self):
        calc = Calculator()
        assert calc.add(2, 3) == 5

    def test_subtract(self):
        calc = Calculator()
        assert calc.subtract(5, 3) == 2

    def test_multiply(self):
        calc = Calculator()
        assert calc.multiply(2, 3) == 6

    def test_divide(self):
        calc = Calculator()
        assert calc.divide(6, 3) == 2.0