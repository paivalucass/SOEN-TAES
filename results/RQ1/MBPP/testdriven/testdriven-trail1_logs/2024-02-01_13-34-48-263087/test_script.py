def is_Diff(n):
    if type(n) != int:
        return False
    if n < 0:
        return False
    # Efficient algorithm for checking divisibility by 11
    # Implementation details to be added based on performance requirements

    # Test cases for different types of input
    if n % 11 == 0:
        return True
    else:
        return False
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Diff(12345), False)

if __name__ == '__main__':
    unittest.main()