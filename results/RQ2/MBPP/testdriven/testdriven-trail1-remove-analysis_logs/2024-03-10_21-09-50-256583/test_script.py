def multiply_num(numbers):
    try:
        if not numbers:
            raise ValueError("Error: Empty list provided")
        if 0 in numbers:
            raise ValueError("Error: Zero found in the list")
        
        result = 1
        for num in numbers:
            result *= num
        
        return result / len(numbers)
    except ZeroDivisionError:
        raise ValueError("Error: Division by zero")
    except Exception as e:
        raise ValueError("Error: " + str(e))
import math
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertTrue(math.isclose(multiply_num((8, 2, 3, -1, 7)), -67.2, rel_tol=0.001))

if __name__ == '__main__':
    unittest.main()