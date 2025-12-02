def list_split(S, step):
    if step <= 0:
        return "Invalid Input"
    result = [S[i:i+step] for i in range(0, len(S), step)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3),
                         [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n']])

if __name__ == '__main__':
    unittest.main()