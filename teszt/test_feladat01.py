from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestParosokSzama(TestCase):
    def test_feladat01(self):
        szamok=[]
        aktualis = feladatok.parosok_szama(szamok)
        elvart = None
        self.assertEqual(elvart, aktualis, "Üres lista esetén nem None a visszatérési érték!")
    def test_feladat02(self):
        szamok=[2]
        aktualis = feladatok.parosok_szama(szamok)
        elvart = 1
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozza meg a listába lévő páros elemek számát!")
    def test_feladat03(self):
        szamok=[1]
        aktualis = feladatok.parosok_szama(szamok)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozza meg a listába lévő páros elemek számát!")
    def test_feladat04(self):
        szamok=[2,3,4]
        aktualis = feladatok.parosok_szama(szamok)
        elvart = 2
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozza meg a listába lévő páros elemek számát!")
    def test_feladat05(self):
        szamok=[2,3,4,2,4,6,1,3]
        aktualis = feladatok.parosok_szama(szamok)
        elvart = 5
        self.assertEqual(elvart, aktualis, "Nem megfelelően határozza meg a listába lévő páros elemek számát!")
