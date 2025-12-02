def closest_num(N):
    closest_number = N - 1
    return closest_number
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(closest_num(11), 10)

if __name__ == '__main__':
    unittest.main()