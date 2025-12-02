def swap_numbers(a, b):
    if a == b:
        return (b, a)
    else:
        return (b, a)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

if __name__ == '__main__':
    unittest.main()