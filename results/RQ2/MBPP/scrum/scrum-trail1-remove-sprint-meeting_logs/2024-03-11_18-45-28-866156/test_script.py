def check_greater(arr, number):
    try:
        if not arr or not all(isinstance(x, (int, float)) for x in arr) or not isinstance(number, (int, float)):
            raise ValueError("Invalid input")
        
        for element in arr:
            if number <= element:
                return False
        return True
    except ValueError as ve:
        return str(ve)
import unittest

class Test(unittest.TestCase):
    def test_check_greater(self):
        self.assertEqual(check_greater([1, 2, 3, 4, 5], 4), False)

if __name__ == '__main__':
    unittest.main()