def is_perfect_square(n):
    if n < 0:
        return False
    if n == 0 or n == 1:
        return True
    
    i = 1
    summ = 0
    while summ < n:
        summ += i
        i += 2
        
    return summ == n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_perfect_square(10), False)

if __name__ == '__main__':
    unittest.main()