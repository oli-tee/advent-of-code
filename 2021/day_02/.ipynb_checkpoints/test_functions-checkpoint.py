import unittest
import module_02

class TestModule02(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(module_02.parse_row('forward 2'), ('forward', 2))

    def test_solve(self):
        self.assertEqual(module_02.solve(['down 10', 'down 20', 'up 5', 'forward 1', 'forward 9']), 250)
        self.assertEqual(module_02.solve(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']), 150)
    
    def test_solve2(self):
        self.assertEqual(module_02.solve2(['forward 5', 'down 5', 'forward 8', 'up 3', 'down 8', 'forward 2']), 900)

if __name__ == '__main__':
    unittest.main()