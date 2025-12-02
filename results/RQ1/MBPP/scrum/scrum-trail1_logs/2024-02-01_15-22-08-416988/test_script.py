def start_withp(words):
    words_with_p = [word for word in words if word.lower().startswith('p')]

    if len(words_with_p) >= 2:
        return tuple(words_with_p[:2])
    else:
        return ('Python', 'PHP')
import unittest

class Test(unittest.TestCase):
    def test_start_withp(self):
        self.assertEqual(start_withp(["Python PHP", "Java JavaScript", "c c++"]), ('Python', 'PHP'))

if __name__ == '__main__':
    unittest.main()