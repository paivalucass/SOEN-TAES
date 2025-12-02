def multiple_to_single(L):
    result = ''
    for num in L:
        if isinstance(num, int):
            result += str(num)
    return int(result) if result else 0
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()