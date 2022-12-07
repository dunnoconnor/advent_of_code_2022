import unittest
from p7a import solve_a
from p7b import solve_b

class Test_P7(unittest.TestCase):
    def test_a(self):
        self.assertEqual(solve_a("sample"), 95437)

    def test_b(self):
        self.assertEqual(solve_b("sample"), 24933642)

if __name__ == '__main__':
    unittest.main()