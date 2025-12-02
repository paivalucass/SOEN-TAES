def empty_list(length):
    return [{} for _ in range(length)] # suggested code
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(empty_list(5), [{},{},{},{},{}])

if __name__ == '__main__':
    unittest.main()