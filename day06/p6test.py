import unittest
from p6a import find_marker

class TestP6(unittest.TestCase):
    def test_a(self):
        self.assertEqual(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb",4),7)

    def test_b(self):
        self.assertEqual(find_marker("mjqjpqmgbljsphdztnvjfqwrcgsmlb",14),19)

if __name__ == '__main__':
    unittest.main()