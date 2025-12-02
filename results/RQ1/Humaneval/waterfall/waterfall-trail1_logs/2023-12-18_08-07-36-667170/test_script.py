def truncate_number(number: float) -> float:
    if number <= 0:
        return 0
    return number - int(number)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(truncate_number(3.5), 0.5)

if __name__ == '__main__':
    unittest.main()