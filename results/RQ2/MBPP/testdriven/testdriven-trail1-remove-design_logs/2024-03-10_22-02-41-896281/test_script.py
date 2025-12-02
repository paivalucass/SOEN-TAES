def swap_numbers(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(swap_numbers(10, 20), (20, 10))

if __name__ == '__main__':
    unittest.main()