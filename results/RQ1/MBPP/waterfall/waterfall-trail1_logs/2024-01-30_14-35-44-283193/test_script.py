def check_Consecutive(l):
    if len(l) < 2:
        return False

    if not all(isinstance(x, int) for x in l):
        return "Error"

    min_num = min(l)
    max_num = max(l)
    if max_num - min_num != len(l) - 1:
        return False

    seen = set()
    for num in l:
        if num in seen:
            return False
        seen.add(num)

    return True
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(check_Consecutive([1,2,3,4,5]), True)

if __name__ == '__main__':
    unittest.main()