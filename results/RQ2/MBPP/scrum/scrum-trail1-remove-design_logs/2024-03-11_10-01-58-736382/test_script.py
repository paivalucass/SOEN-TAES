def len_log(list1):
    if not list1 or not all(isinstance(x, str) for x in list1):
        return 0
    return max(len(x) for x in list1)
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(len_log(["python", "PHP", "bigdata"]), 7)

if __name__ == '__main__':
    unittest.main()