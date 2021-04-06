import unittest
import math_library



class TestADD(unittest.TestCase):
   def ADDnuber(self):
      result=ADD(1.00012, 1.00012 )
      self.assertEqual(result, 1.00024)
      result=ADD(1000000000000, 1000000000000 )
      self.assertEqual(result, 2000000000000)
      result=ADD(5,-7)
      self.assertEqual(result,-2)
      result=ADD(0,12)
      self.assertEqual(result, 12)
   def ADDstring(self):
      self.assertRaises(wronginput,ADD("ad",6))
      self.assertRaises(wronginput,ADD(6,"ad"))
      self.assertRaises(wronginput,ADD("ad","ad"))

class TestSUB(unittest.TestCase):        
   def SUBnumber(self):
      result=SUB(1.00012, 1.00011 )
      self.assertEqual(result, 0.00001)
      result=SUB(1000000000000, 100000000000 )
      self.assertEqual(result, 900000000000)
      result=SUB(5,-7)
      self.assertEqual(result,12)
      result=SUB(0,12)
      self.assertEqual(result, -12)
   def SUBstring(self):
      self.assertRaises(wronginput,SUB("ad",6))
      self.assertRaises(wronginput,SUB(6,"ad"))
      elf.assertRaises(wronginput,SUB("ad","ad"))

class TestDIV(unittest.TestCase):
   def DIVnumber(self):
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
      self.assertRaises(wronginput,DIV(10,0))
   def DIVstring(self):
      self.assertRaises(wronginput,DIV("ad",6))
      self.assertRaises(wronginput,DIV(6,"ad"))
      self.assertRaises(wronginput,DIV("ad","ad"))

class TestSQRT(unittest.TestCase):
   def SQRTnumber(self):
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
      self.assertRaises(wronginput,SQRT(-5))
      self.assertRaises(wronginput,SQRT(-459))
   def SQRTstring(self):
      self.assertRaises(wronginput,SQRT("ad"))
class TestMUL(unittest.TestCase):
   def MULnumber(self):
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
   def MULstring(self):
      self.assertRaises(wronginput,MUL("ad",6))
      self.assertRaises(wronginput,MUL(6,"ad"))
      self.assertRaises(wronginput,MUL("ad","ad"))

class TestPOW(unittest.TestCase):
   def POWnumber(self):
      result=POW(1)
      self.assertEqual(result, 1*1)
      result=POW(2)
      self.assertEqual(result, 2*2)
      result=POW(50)
      self.assertEqual(result, 50*50)
      result=POW(-20)
      self.assertEqual(result, -20*-20)

   def POWstring(self):
      self.assertRaises(wronginput,POW("ad")

if __name__ == '__main__':
   unittest.main()
