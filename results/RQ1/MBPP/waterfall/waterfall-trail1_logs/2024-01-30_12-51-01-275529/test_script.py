def division_elements(test_tup1, test_tup2):
    result = ()
    try:
        if len(test_tup1) != len(test_tup2):
            raise ValueError("Input tuples must be of the same length")
        result = tuple(x / y for x, y in zip(test_tup1, test_tup2))
    except ZeroDivisionError:
        print("Error: Division by zero")
    except TypeError:
        print("Error: Invalid input type")
    except ValueError as ve:
        print("Error:", ve)
    except Exception as e:
        print("An error occurred:", str(e))
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(division_elements((10, 4, 6, 9),(5, 2, 3, 3)), (2, 2, 2, 3))

if __name__ == '__main__':
    unittest.main()