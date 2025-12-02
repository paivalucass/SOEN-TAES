def find_volume(length, base, height):
    if not all(isinstance(i, int) for i in [length, base, height]) or any(i <= 0 for i in [length, base, height]):
        return "Invalid input"
    else:
        return length * base * height

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Volume(10, 8, 6), 240)

if __name__ == '__main__':
    unittest.main()