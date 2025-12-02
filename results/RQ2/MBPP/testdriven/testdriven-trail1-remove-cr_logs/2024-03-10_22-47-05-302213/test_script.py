def get_ludic(n):
    result = []
    for num in range(1, n+1):
        if all(num % i != 0 for i in range(2, num)):
            result.append(num)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(get_ludic(10), [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()