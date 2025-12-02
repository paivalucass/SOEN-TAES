def multiple_to_single(integers_list):
    return int(''.join(map(str, integers_list)))
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(multiple_to_single([11, 33, 50]), 113350)

if __name__ == '__main__':
    unittest.main()