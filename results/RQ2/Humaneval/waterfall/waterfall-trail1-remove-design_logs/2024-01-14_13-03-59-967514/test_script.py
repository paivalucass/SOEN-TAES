def truncate_number(number: float) -> float:
    if isinstance(number, float):
        return round(number - int(number), 15)
    else:
        raise ValueError("Input is not a valid float number")

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(truncate_number(3.5), 0.5)

if __name__ == '__main__':
    unittest.main()