def is_Even(n: int) -> bool:
    '''Write a python function to check whether the given number is even or not.
    assert is_Even(1) == False
    '''
    if isinstance(n, int):
        return n % 2 == 0
    else:
        raise ValueError("Input must be an integer")
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_Even(1), False)

if __name__ == '__main__':
    unittest.main()