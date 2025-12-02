def catalan_number(num):
    if num < 0:
        return "Invalid input"
    elif num <= 1:
        return 1

    res = [0] * (num + 1)
    res[0] = 1

    for i in range(1, num + 1):
        for j in range(i):
            res[i] += res[j] * res[i - j - 1]

    return res[num]
import unittest

class Test(unittest.TestCase):
    def test_catalan_number(self):
        self.assertEqual(catalan_number(10), 16796)

if __name__ == '__main__':
    unittest.main()