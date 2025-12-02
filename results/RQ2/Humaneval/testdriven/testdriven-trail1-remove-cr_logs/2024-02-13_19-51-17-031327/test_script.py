def add_elements(arr, k):
    sum = 0
    count = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            sum += arr[i]
            count += 1
        if count == k:
            break
    return sum

import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(add_elements([111,21,3,4000,5,6,7,8,9], 4), 24)

if __name__ == '__main__':
    unittest.main()