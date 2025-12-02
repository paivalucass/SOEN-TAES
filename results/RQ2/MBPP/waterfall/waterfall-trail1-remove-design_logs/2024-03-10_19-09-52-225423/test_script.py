import math
def next_Perfect_Square(N):
    return math.ceil(N ** 0.5) ** 2
import math

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(next_Perfect_Square(35), 36)

if __name__ == '__main__':
    unittest.main()