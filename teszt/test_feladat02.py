from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class HanyTargybolBukik(TestCase):
    def test_feladat02(self):
        szamok=[1]
        aktualis = feladatok.hany_targybol_bukik(szamok)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozta meg a bukások számát!")
    def test_feladat03(self):
        szamok=[5]
        aktualis = feladatok.hany_targybol_bukik(szamok)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozta meg a bukások számát!")
    def test_feladat04(self):
        szamok=[1,3,1]
        aktualis = feladatok.hany_targybol_bukik(szamok)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozta meg a bukások számát!")
    def test_feladat05(self):
        szamok=[2,1,4,2,1,6,1,1]
        aktualis = feladatok.hany_targybol_bukik(szamok)
        elvart = 4
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozta meg a bukások számát!")
