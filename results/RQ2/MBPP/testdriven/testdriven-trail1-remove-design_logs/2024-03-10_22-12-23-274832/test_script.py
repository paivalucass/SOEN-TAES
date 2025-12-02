def catalan_number(num):
    '''Write a function which returns nth catalan number.'''
    
    if num < 0:
        return "Invalid Input"
    elif num == 0:
        return 1
    else:
        result = 1
        for i in range(1, num + 1):
            result = result * (4 * i - 2) // (i + 1)
        return result

assert catalan_number(10)==16796
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()