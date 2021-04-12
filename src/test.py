import unittest
from mathLib import *
import math

class TestADD(unittest.TestCase):
   def testADDnuber(self):
      result=ADD(1.00012, 1.00012)
      self.assertEqual(result, 2.00024)
      result=ADD(1000000000000, 1000000000000)
      self.assertEqual(result, 2000000000000)
      result=ADD(5,-7)
      self.assertEqual(result,-2)
      result=ADD(0,12)
      self.assertEqual(result, 12)
   def testADDstring(self):
      with self.assertRaises(TypeError):
         ADD("ad",6)
      with self.assertRaises(TypeError):
         ADD(6,"ad")
      with self.assertRaises(TypeError):
         ADD("ad","ad")

class TestSUB(unittest.TestCase):        
   def testSUBnumber(self):
      result=SUB(1000000000000, 100000000000 )
      self.assertEqual(result, 900000000000)
      result=SUB(5,-7)
      self.assertEqual(result,12)
      result=SUB(0,12)
      self.assertEqual(result, -12)
   def testSUBstring(self):
      with self.assertRaises(TypeError):
         SUB("ad",6)
      with self.assertRaises(TypeError):
         SUB(6,"ad")
      with self.assertRaises(TypeError):
         SUB("ad","ad")

class TestDIV(unittest.TestCase):
   def testDIVnumber(self):
      result=DIV(5000, 5)
      self.assertEqual(result, 1000)
      result=DIV(10, 3)
      self.assertEqual(result, (10.0/3.0))
      result=DIV(5, 5)
      self.assertEqual(result, 1)
      result=DIV(-325, 5)
      self.assertEqual(result, -65)
      result=DIV(-10, -2)
      self.assertEqual(result, 5)
      with self.assertRaises(ZeroDivisionError):
         DIV(10,0)
   def testDIVstring(self):
      with self.assertRaises(TypeError):
         DIV("ad",6)
      with self.assertRaises(TypeError):
         DIV(6,"ad")
      with self.assertRaises(TypeError):
         DIV("ad","ad")

class TestSQRT(unittest.TestCase):
   def testSQRTnumber(self):
      result=SQRT(25)
      self.assertEqual(result, 5)
      result=SQRT(0)
      self.assertEqual(result, 0)
      result=SQRT(159)
      self.assertEqual(result, math.sqrt(159))
      result=SQRT(135429.123456)
      self.assertEqual(result, math.sqrt(135429.123456))
      result=SQRT(10000000000000000)
      self.assertEqual(result, math.sqrt(10000000000000000))
      with self.assertRaises(ValueError):
         SQRT(-5)
      with self.assertRaises(ValueError):
         SQRT(-459)
   def testSQRTstring(self):
      with self.assertRaises(TypeError):
         SQRT("ad")

class TestROOT(unittest.TestCase):
   def testROOTnumber(self):
      result=ROOT(25, 2)
      self.assertEqual(result, 5)
      result=ROOT(0, 10)
      self.assertEqual(result, 0)
      result=ROOT(159, 4)
      self.assertEqual(result, 159**(1/4))
      result=ROOT(-216, 3)
      self.assertTrue(math.isclose(result, -6, rel_tol=1e-5))
      result=ROOT(1000000000000000, 5)
      self.assertTrue(math.isclose(result, 1000, rel_tol=1e-5))
      with self.assertRaises(ValueError):
         ROOT(-5, 4)
   def testSQRTstring(self):
      with self.assertRaises(TypeError):
         ROOT("ad",6)
      with self.assertRaises(TypeError):
         ROOT(6,"ad")
      with self.assertRaises(TypeError):
         ROOT("ad","ad")

class TestMUL(unittest.TestCase):
   def testMULnumber(self):
      result=MUL(10, 10)
      self.assertEqual(result, 100)
      result=MUL(1.23, 1.54)
      self.assertEqual(result, 1.8942)
      result=MUL(500000, 0)
      self.assertEqual(result, 0)
      result=MUL(0.5, 0.5)
      self.assertEqual(result, 0.25)
      result=MUL(-10, 10)
      self.assertEqual(result, -100)
      result=MUL(-10, -10)
      self.assertEqual(result, 100)
   def testMULstring(self):
      with self.assertRaises(TypeError):
         MUL("ad",6)
      with self.assertRaises(TypeError):
         MUL(6,"ad")
      with self.assertRaises(TypeError):
         MUL("ad","ad")

class TestPOW(unittest.TestCase):
   def testPOWnumber(self):
      result = POW(1, 1)
      self.assertEqual(result, 1)
      result = POW(2, 2)
      self.assertEqual(result, 4)
      result = POW(50, 5)
      self.assertEqual(result, 312500000)
      result = POW(-20, 0)
      self.assertEqual(result, 1)
      result = POW(-20, -2)
      self.assertEqual(result, 0.0025)

   def testPOWstring(self):
      with self.assertRaises(TypeError):
         POW("ad",6)
      with self.assertRaises(TypeError):
         POW(6,"ad")
      with self.assertRaises(TypeError):
         POW("ad","ad")

if __name__ == '__main__':
   unittest.main()
