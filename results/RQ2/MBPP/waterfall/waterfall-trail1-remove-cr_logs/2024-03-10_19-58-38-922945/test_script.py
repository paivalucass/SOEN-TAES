def list_split(S, step):
    result = []
    if step <= 0 or step > len(S):
        return result
    for i in range(step):
        sublist = S[i::step]
        result.append(sublist)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()