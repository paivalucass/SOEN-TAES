def get_max_triples(n):
    result = 0
    a = [(i * i - i + 1) % 3 for i in range(1, n + 1)]
    count = [0, 0, 0]
    
    for i in range(n):
        count[a[i]] += 1
    
    result += count[0] * (count[0] - 1) * (count[0] - 2) // 6
    result += count[1] * (count[1] - 1) * (count[1] - 2) // 6
    result += count[2] * (count[2] - 1) * (count[2] - 2) // 6
    result += count[0] * count[1] * count[2]
    
    return result
import unittest

class Test(unittest.TestCase):
    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(5), 1)

if __name__ == '__main__':
    unittest.main()