def truncate_number(number: float) -> float:
    return number - int(number)
import unittest

class Test(unittest.TestCase):
    def test_truncate_number(self):
        self.assertEqual(truncate_number(3.5), 0.5)
        self.assertEqual(truncate_number(0.75), 0.75)
        self.assertEqual(truncate_number(10), 0)
        self.assertEqual(truncate_number(5.9), 0.9)

if __name__ == '__main__':
    unittest.main()