def highest_Power_of_2(n):
    power = 0
    result = 1
    while result <= n:
        result = 2 ** power
        if result <= n:
            power += 1
        else:
            power -= 1
            result = 2 ** power
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(highest_Power_of_2(10), 8)

if __name__ == '__main__':
    unittest.main()