import re

def find_adverbs(text):
    match = re.search(r'\b\w+ly\b', text)
    if match:
        return f"{match.start()}-{match.end()}: {match.group()}"
    else:
        return None
import re

class Test(unittest.TestCase):
    def test(self):
        self.assertEqual(find_adverbs("Clearly, he has no excuse for such behavior."), '0-7: Clearly')

if __name__ == '__main__':
    unittest.main()