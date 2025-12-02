def start_withp(words):
    result = []
    for word in words:
        if word.startswith('p') or word.startswith('P'):
            result.extend(word.split())
    return tuple(result)

import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()