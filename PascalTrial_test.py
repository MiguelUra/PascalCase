import unittest
import math
class TestClass(unittest.TestCase):
    def Espacios_test(self):
        strng1 = "Hola soy de malacia"
        strng2 = "Hola Soy De Malacia"
        z =""
        Splitter = strng1.split(" ")
        for i in range(0, len(Splitter)):
            z += Splitter[i].capitalize() + " "
        United = " ".join(z.split())
        self.assertEqual(strng2, United)
class TestClasss(unittest.TestCase):
    def Otraprueba_test(self):
        m = "la vida es bella"
        n = "la Vida es Bella"
        z = ""
        spltr = m.split(" ")
        for i in range(0, len(spltr)):
            z += spltr[i].capitalize() + " "
        convertion = " ".join(z.split())
        self.assertEqual(n, convertion)
if __name__ == '__main__':
    unittest.main()