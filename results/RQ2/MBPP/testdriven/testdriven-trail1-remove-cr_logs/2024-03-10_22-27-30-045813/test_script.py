def find_Volume(l, b, h):
    try:
        if l <= 0 or b <= 0 or h <= 0:
            raise ValueError("Input values for length, breadth, and height must be positive numbers")
        volume = (1/2) * l * b * h
        return volume
    except ValueError as ve:
        return f"Error: {ve}"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()