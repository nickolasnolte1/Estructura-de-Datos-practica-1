import cProfile
import unittest
import defsumatoria

class TestMyModule(unittest.TestCase):
    
    def test_defsumatoria(self):
        self.assertEqual(mymodule.sum(5, 7), 12)
if __name__ == "__main__":
    unittest.main()
    
number = int(input("Escriba un número entero positivo: "))

valortotal = sumatoria(number)

print("La sumatoria de los números naturales del 1 al {0} es: {1}".format(number, valortotal))


cProfile.run ('sumatoria(5)')

if __name__ == "__main__":
    unittest.main()