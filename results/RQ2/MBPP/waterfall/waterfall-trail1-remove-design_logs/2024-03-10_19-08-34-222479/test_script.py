def next_power_of_2(n):
    if isinstance(n, int) and n >= 0:
        if n == 0:
            return 1
        else:
            return 2**(math.ceil(math.log2(n)))
    else:
        return "Invalid Input"
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_power_of_2(0), 1)

if __name__ == '__main__':
    unittest.main()