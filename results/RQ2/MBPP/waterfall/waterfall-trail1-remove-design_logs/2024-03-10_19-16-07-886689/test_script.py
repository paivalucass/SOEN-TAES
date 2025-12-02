def neg_nos(list1):
    if all(isinstance(num, (int, float)) for num in list1):
        return [num for num in list1 if num < 0]
    else:
        raise ValueError("Input list should contain only numbers")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(neg_nos([-1, 4, 5, -6]), [-1, -6])

if __name__ == '__main__':
    unittest.main()