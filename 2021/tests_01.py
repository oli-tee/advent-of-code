import unittest
import module_01

class TestStringMethods(unittest.TestCase):

    def test_solve(self):
 
        self.assertEqual(module_01.solve([0,1,0,2]), 2)

        self.assertEqual(module_01.solve([10, 9, 8, 7], 0)

        self.assertEqual(module_01.solve([1,2,3,4], 3)

if __name__ == '__main__':
    unittest.main()