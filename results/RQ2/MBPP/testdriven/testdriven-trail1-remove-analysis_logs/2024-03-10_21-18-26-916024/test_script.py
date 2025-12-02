def remove_odd(l):
    return [num for num in l if num % 2 == 0]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(remove_odd([1,2,3]), [2])

if __name__ == '__main__':
    unittest.main()