def fizz_buzz(n: int):
    count = 0
    for i in range(n):
        if i % 11 == 0 or i % 13 == 0:
            count += str(i).count('7')
    return count

import unittest

class Test(unittest.TestCase):
    def test_fizz_buzz(self):
        self.assertEqual(fizz_buzz(50), 0)
        self.assertEqual(fizz_buzz(78), 2)
        self.assertEqual(fizz_buzz(79), 3)

if __name__ == '__main__':
    unittest.main()