def is_Even(n):
    try:
        if isinstance(n, int):
            return n % 2 == 0
        else:
            raise ValueError("Input is not an integer")
    except ValueError as e:
        print(e)
        return False

# Test cases
assert is_Even(1) == False
assert is_Even(2) == True
assert is_Even(0) == True
assert is_Even(-1) == False
assert is_Even(1000000000000000000000000000000000000000000000000000000000000000000000000000) == True
assert is_Even(-1000000000000000000000000000000000000000000000000000000000000000000000000001) == False
assert is_Even("string") == False
import unittest

class Test(unittest.TestCase):
    def test_is_Even(self):
        self.assertEqual(is_Even(1), False)

if __name__ == '__main__':
    unittest.main()