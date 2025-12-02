def list_split(S, step):
    if len(S) == 0 or step <= 0:
        return []

    result_list = []
    for i in range(step):
        sublist = S[i::step]
        result_list.append(sublist)
    
    return result_list
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()