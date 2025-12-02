def hexagonal_num(n: int) -> int:
    if type(n) != int:
        return "Error"
    if n < 0:
        return 2 * n**2 - n
    return 2 * n**2 - n
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(hexagonal_num(10), 190)

if __name__ == '__main__':
    unittest.main()