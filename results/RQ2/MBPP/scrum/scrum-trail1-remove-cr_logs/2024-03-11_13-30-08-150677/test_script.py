def digit_distance_nums(n1, n2):
    if not isinstance(n1, int) or not isinstance(n2, int):
        return "Error: Non-integer inputs"

    if n1 is None or n2 is None:
        return "Error: Null or empty inputs"
    
    if len(str(n1)) != len(str(n2)):
        raise ValueError("Input integers must have the same number of digits")

    total_distance = 0
    for digit1, digit2 in zip(str(n1), str(n2)):
        total_distance += abs(int(digit1) - int(digit2))
    
    return total_distance
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(digit_distance_nums(1, 2), 1)

if __name__ == '__main__':
    unittest.main()