def count_occurrence(s, sub):
    if not isinstance(s, str) or not isinstance(sub, str):
        return 'Error: Both inputs must be strings'
    count = 0
    s = s.lower()
    sub = sub.lower()
    i = s.find(sub)
    while i != -1:
        count += 1
        i = s.find(sub, i + 1)
    return count

assert count_occurrence("letstdlenstdporstd", "std") == 3
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(count_occurance("letstdlenstdporstd"), 3)

if __name__ == '__main__':
    unittest.main()