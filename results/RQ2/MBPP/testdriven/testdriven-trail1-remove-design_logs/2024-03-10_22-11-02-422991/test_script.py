def digit_distance_nums(n1, n2):
    try:
        if not isinstance(n1, int) or not isinstance(n2, int):
            raise TypeError("Input values must be integers")
        
        return abs(n1 - n2)
    except TypeError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()