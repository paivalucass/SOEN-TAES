def sequence(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        sequence_list = [0, 1, 1]
        for i in range(3, n+1):
            sequence_list.append(sequence_list[sequence_list[i - 1]] + sequence_list[i - sequence_list[i - 1]])
        return sequence_list[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()