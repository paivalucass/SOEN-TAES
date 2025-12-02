def square_perimeter(side_length):
    assert side_length >= 0, "Side length must be a non-negative value"
    perimeter = 4 * side_length
    return perimeter
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(square_perimeter(10), 40)

if __name__ == '__main__':
    unittest.main()