def is_undulating(n: int) -> bool:
    '''Check whether the given number is undulating or not.'''
    digits = [int(d) for d in str(n)]
    is_undulating = all(digits[i] < digits[i+1] > digits[i+2] if i % 2 == 0 else digits[i] > digits[i+1] < digits[i+2] for i in range(len(digits)-2))
    return is_undulating
import unittest

class Test(unittest.TestCase):
    def test_is_undulating(self):
        self.assertEqual(is_undulating(1212121), True)

if __name__ == '__main__':
    unittest.main()