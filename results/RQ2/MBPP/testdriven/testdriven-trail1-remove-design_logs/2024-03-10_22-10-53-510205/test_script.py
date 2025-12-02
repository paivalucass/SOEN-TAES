def find_odd_xor_pairs(arr, length):
    if length <= 0:
        return "Invalid input"
    count = 0
    for i in range(length):
        for j in range(i+1, length):
            if (arr[i] ^ arr[j]) % 2 != 0:
                count += 1
    return count

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_Odd_Pair([5,4,7,2,1],5), 6)

if __name__ == '__main__':
    unittest.main()