import math

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        # Static method: doesn't use the class or instance
        return a + b

    @classmethod
    def multiply(cls, a, b):
        # Class method: accesses class attribute
        print(f"Calculation type: {cls.calculation_type}")
        return a * b

