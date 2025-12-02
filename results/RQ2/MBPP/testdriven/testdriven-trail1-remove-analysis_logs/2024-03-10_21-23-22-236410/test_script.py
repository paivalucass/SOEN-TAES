def catalan_number(num):
    '''
    Write a function which returns nth catalan number.
    assert catalan_number(10)==16796
    '''
    if num < 0:
        return "Error: Invalid input"
    elif num == 0:
        return 1
    else:
        c = 1
        for i in range(0, num):
            c = c * 2 * (2 * i + 1) / (i + 2)
        return c
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()