def division_elements(test_tup1, test_tup2):
    try:
        if isinstance(test_tup1, tuple) and isinstance(test_tup2, tuple):
            if len(test_tup1) != len(test_tup2):
                raise ValueError("Tuples have different lengths")
            result = tuple(map(lambda x, y: x / y, test_tup1, test_tup2))
            return result
        else:
            raise TypeError("Input parameters test_tup1 and test_tup2 must be tuples")
    except ZeroDivisionError:
        return "Error: Division by zero"
    except TypeError:
        return "Error: Invalid input parameters, expected tuples"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: {e}"
import unittest

class Test(unittest.TestCase):
    def test_division_elements(self):
        self.assertEqual(division_elements((10, 4, 6, 9), (5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()