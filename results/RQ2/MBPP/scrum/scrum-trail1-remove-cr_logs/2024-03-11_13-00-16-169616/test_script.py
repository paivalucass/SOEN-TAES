def list_split(S, step):
    result = []
    for i in range(0, len(S), step):
        result.append(S[i:i+step])
    return result
import unittest

class TestListSplit(unittest.TestCase):
    
    def test_list_split(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n']])
      
if __name__ == '__main__':
    unittest.main()