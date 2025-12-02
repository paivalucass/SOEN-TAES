def pos_count(list):
    if not list:
        return 0
    if not all(isinstance(num, (int, float)) for num in list):
        return "Invalid Input"
    pos_count = 0
    for num in list:
        if num > 0:
            pos_count += 1
    return pos_count
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(pos_count([1,-2,3,-4]), 2)

if __name__ == '__main__':
    unittest.main()