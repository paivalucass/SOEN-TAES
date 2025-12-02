def catalan_number(num):
    if num < 0:
        return 'Invalid input'
    if num == 0:
        return 1
    result = 1
    for i in range(1, num + 1):
        result = result * (2 * (2 * i - 1)) / (i + 1)
    return int(result)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()