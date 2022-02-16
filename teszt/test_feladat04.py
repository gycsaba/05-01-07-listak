from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestHianyzasok(TestCase):
    def test_hianyzasok01(self):
        szamok=[]
        aktualis = feladatok.hianyzasok_atlaga(szamok)
        elvart = None
        self.assertEqual(elvart, aktualis, "Hiányzások számát nem jól határozta meg")
    def test_hianyzasok02(self):
        szamok=[0,0,0,0,0,0]
        aktualis = feladatok.hianyzasok_atlaga(szamok)
        elvart = 0
        self.assertEqual(elvart, aktualis, "Hiányzások számát nem jól határozta meg")
    def test_hianyzasok03(self):
        szamok=[5,5,5,5,5]
        aktualis = feladatok.hianyzasok_atlaga(szamok)
        elvart = 5
        self.assertEqual(elvart, aktualis, "Hiányzások számát nem jól határozta meg")
    def test_hianyzasok04(self):
        szamok=[0,6,4,0,0,0]
        aktualis = feladatok.hianyzasok_atlaga(szamok)
        elvart = 1.6666666666666667
        self.assertEqual(elvart, aktualis, "Hiányzások számát nem jól határozta meg")
    def test_hianyzasok05(self):
        szamok=[0,6,4,0,0,0,7,0,0,0]
        aktualis = feladatok.hianyzasok_atlaga(szamok)
        elvart = 1.7
        self.assertEqual(elvart, aktualis, "Hiányzások számát nem jól határozta meg")