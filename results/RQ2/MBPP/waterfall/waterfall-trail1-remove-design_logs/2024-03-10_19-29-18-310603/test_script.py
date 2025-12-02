def check_Consecutive(l):
    if not l:
        return False

    if not all(isinstance(x, (int, float)) for x in l):
        return False

    sorted_list = sorted(l)
    for i in range(1, len(sorted_list)):
        if sorted_list[i] != sorted_list[i-1] + 1:
            return False
    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()