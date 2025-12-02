def sequence(n):
    if n == 0:
        return "Invalid input"
    elif n <= 2:
        return "1"
    else:
        newman_conway_sequence = [0, 1, 1]
        for i in range(3, n + 1):
            newman_conway_sequence.append(newman_conway_sequence[newman_conway_sequence[i - 1]] + newman_conway_sequence[i - newman_conway_sequence[i - 1]])
        return newman_conway_sequence[n]
import unittest

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(sequence(10), 6)

if __name__ == '__main__':
    unittest.main()