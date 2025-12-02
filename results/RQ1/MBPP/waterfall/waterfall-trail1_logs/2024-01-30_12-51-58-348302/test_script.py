def list_split(S, step):
    if not isinstance(S, list) or not isinstance(step, int) or step <= 0:
        return "Invalid input: S must be a list and step must be a positive integer."

    result = [S[i::step] for i in range(step)]
    return result
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()