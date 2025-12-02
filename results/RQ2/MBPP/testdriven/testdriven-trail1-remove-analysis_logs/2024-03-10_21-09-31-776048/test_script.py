def power(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Input parameters 'a' and 'b' must be numbers")
    if b < 0:
        raise ValueError("Input parameter 'b' must be a non-negative number")

    try:
        result = a ** b
        return result
    except OverflowError:
        return "Error: Result too large to compute"
    except Exception as e:
        return "Error: {}".format(e)
import unittest

class Test(unittest.TestCase):
    def test_power_function(self):
        self.assertEqual(power(3, 4), 81)

if __name__ == '__main__':
    unittest.main()