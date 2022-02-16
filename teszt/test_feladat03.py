from unittest import TestCase

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
import feladatok

class TestOrak(TestCase):
    def test_feladat01(self):
        szamok=[]
        aktualis = feladatok.heti_orak_atlaga(szamok)
        elvart = None
        self.assertEqual(elvart, aktualis, "Órák átlagát nem jól határozta megg")
    def test_feladat02(self):
        szamok=[5,5,5,5,5,5]
        aktualis = feladatok.heti_orak_atlaga(szamok)
        elvart = 5
        self.assertEqual(elvart, aktualis, "Órák átlagát nem jól határozta megg")
    def test_feladat03(self):
        szamok=[5,6,7,7,5]
        aktualis = feladatok.heti_orak_atlaga(szamok)
        elvart = 6
        self.assertEqual(elvart, aktualis, "Órák átlagát nem jól határozta megg")
    def test_feladat04(self):
        szamok=[5,6,7,8,5]
        aktualis = feladatok.heti_orak_atlaga(szamok)
        elvart = 6.2
        self.assertEqual(elvart, aktualis, "Órák átlagát nem jól határozta megg")