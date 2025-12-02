def is_polite(n):
    count = 0
    num = 1
    while(count < n):
        num += 1
        if (isPolite(num)):
            count += 1
    return num

# Helper function to check if a number is polite
# geeksforgeeks.org/n-th-polite-number/
def isPolite(num):
    if(num % 2 == 0):
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if(num % i == 0):
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(is_polite(7), 11)

if __name__ == '__main__':
    unittest.main()