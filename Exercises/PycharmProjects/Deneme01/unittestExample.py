##Sample unittest
import unittest

class deneme(unittest.TestCase):

    def test(self):
        str='deneme'
        self.assertEqual(str, 'deneme')

##Bu kısım, eğer ki dosya importlanırarak çalıştırılırsa, çalışmasını önlüyor. (Yanlış olabilir)
if __name__=='__main__':
    unittest.main()