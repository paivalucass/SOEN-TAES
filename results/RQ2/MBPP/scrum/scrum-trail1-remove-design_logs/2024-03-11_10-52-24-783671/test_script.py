def catalan_number(num):
    if num <= 1:
        return 1
    
    catalan = [0] * (num + 1)
    catalan[0] = 1
    catalan[1] = 1
    
    for i in range(2, num + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]
    
    return catalan[num]
import unittest

class Test(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()