def ascii_value(k: str) -> int:
    if len(k) != 1:
        raise ValueError("Input must be a single character")
    return ord(k)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(ascii_value('A'), 65)

if __name__ == '__main__':
    unittest.main()