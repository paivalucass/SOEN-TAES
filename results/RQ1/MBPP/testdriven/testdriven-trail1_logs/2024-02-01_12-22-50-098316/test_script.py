def list_split(S, step):
    if not isinstance(S, list) or step <= 0:
        raise ValueError("Invalid input")
    result = []
    for i in range(step):
        sub_list = []
        for j in range(i, len(S), step):
            sub_list.append(S[j])
        result.append(sub_list)
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()