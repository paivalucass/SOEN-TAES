def get_max_triples(n):
    count = 0
    a = [i * i - i + 1 for i in range(1, n + 1)]
    a_mod_3 = [x % 3 for x in a]
    
    count_dict = {0: 0, 1: 0, 2: 0}
    for i in a_mod_3:
        count_dict[i] += 1
    
    count += count_dict[0] * (count_dict[0] - 1) * (count_dict[0] - 2) // 6  # combination of choosing 3 elements from count_dict[0]
    count += count_dict[1] * count_dict[2] * count_dict[0]  # combination of choosing 1 element from count_dict[1] and 1 element from count_dict[2] and 1 element from count_dict[0]
    count += count_dict[2] * (count_dict[2] - 1) * (count_dict[2] - 2) // 6  # combination of choosing 3 elements from count_dict[2]

    return count

import unittest

class Test(unittest.TestCase):
    def test_get_max_triples(self):
        self.assertEqual(get_max_triples(5), 1)

if __name__ == '__main__':
    unittest.main()