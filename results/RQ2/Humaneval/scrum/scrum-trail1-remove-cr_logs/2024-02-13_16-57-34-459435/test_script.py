def add(x: int, y: int):
    """
    Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    if not isinstance(x, int) or not isinstance(y, int):
        return "Error: Non-integer input"
    
    try:
        result = x + y
        if (x > 0 and y > 0 and result < 0) or (x < 0 and y < 0 and result > 0):
            raise OverflowError("Addition result is out of range")
        return result
    except OverflowError:
        return "Error: Potential overflow"
    except:
        return "Error: Potential underflow"
import unittest

class Test(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(5, 7), 12)

if __name__ == '__main__':
    unittest.main()