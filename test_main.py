import unittest
from main import get_random_proverb
class TestMain(unittest.TestCase):
    def test_get_random_proverb_returns_string(self):
        result = get_random_proverb()
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)
if __name__ == '__main__':
    unittest.main()
