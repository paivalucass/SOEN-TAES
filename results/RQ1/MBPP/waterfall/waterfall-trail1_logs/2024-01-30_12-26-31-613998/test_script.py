def closest_num(input_number):
    if not isinstance(input_number, (int, float)):
        return "Invalid input"
    if input_number <= 0:
        return "Invalid input"
    
    closest_smaller = input_number - 1
    
    return closest_smaller
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()