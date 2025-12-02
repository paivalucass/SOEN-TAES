def is_polite(n):
    if n <= 0:
        raise ValueError("Input value should be a positive integer")
    if n == 1:
        return 1
    count = 1
    num = 2
    while(count < n):
        num += 1
        num_of_div = 0
        for i in range(1, num+1):
            if(num % i == 0):
                num_of_div += 1
        if(num_of_div == 3):
            count += 1
    return num
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()