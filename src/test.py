import unittest
import math_library



class TestADD(unittest.TestCase):
    def addnuber(self):
        result=soucet(1.00012, 1.00012 )
        self.assertEqual(result, 1.00024)
        result=soucet(5,-7)
        self.assertEqual(result,-2)
        result=soucet(0,12)
        self.assertEqual(result, 12)
     def addstring(self):
        elf.assertRaises(wronginput,soucet("ad",6))

if __name__ == '__main__':
    unittest.main()