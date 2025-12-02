def catalan_number(num):
    if num < 0:
        return "Negative input not allowed"
    elif num == 0:
        return 1
    else:
        catalan = [0] * (num + 1)
        catalan[0] = 1
        for i in range(1, num + 1):
            catalan[i] = 0
            for j in range(i):
                catalan[i] += catalan[j] * catalan[i - j - 1]
        
        return catalan[num]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()