def list_split(S, step):
    if step <= 0 or not isinstance(step, int):
        return "Invalid input for parameter2"

    result = [[] for _ in range(step)]
    for i in range(len(S)):
        result[i % step].append(S[i])

    return [x for x in result if x]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(list_split(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'], 3), [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']])

if __name__ == '__main__':
    unittest.main()