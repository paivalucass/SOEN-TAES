def sequence(n):
    '''Write a function to find the nth number in the newman conway sequence.
    assert sequence(10) == 6'''
    
    if n == 0:
        return "Invalid input"
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        result = {1: 1, 2: 1}
        for i in range(3, n+1):
            result[i] = result[result[i - 1]] + result[i - result[i - 1]]
        return result[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()