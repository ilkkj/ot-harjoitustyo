import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kassassa_rahaa = 100000
        self.riittava_maksu = 500
        self.ei_riittava_maksu = 100

        self.edullinen = 240
        self.maukas = 400

        self.maksukortti_riittava = Maksukortti(500)
        self.maksukortti_ei_riittava = Maksukortti(100)
        self.maksukortti_tyhja = Maksukortti(0)
    
    def test_alussa_rahamaara_ja_myydyt_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kassan_rahamaara_ja_myydyt_kasvaa_oikein_kun_maksu_edulliseen_on_riittava(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(self.riittava_maksu), self.riittava_maksu - self.edullinen)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa + self.edullinen)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_kassan_rahamaara_ja_myydyt_kasvaa_oikein_kun_maksu_maukkaaseen_on_riittava(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(self.riittava_maksu), self.riittava_maksu - self.maukas)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa + self.maukas)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_kassan_rahamaara_ja_myydyt_ei_muutu_jos_maksu_ei_riittava_edulliseen(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(self.ei_riittava_maksu), self.ei_riittava_maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_kassan_rahamaara_ja_myydyt_ei_muutu_jos_maksu_ei_riittava_maukkaaseen(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(self.ei_riittava_maksu), self.ei_riittava_maksu)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_korttiosto_edulliselle_toimii_jos_kortilla_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_riittava))
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa)

    def test_korttiosto_maukkaalle_toimii_jos_kortilla_tarpeeksi_rahaa(self):
        self.assertTrue(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_riittava))
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa)

    def test_korttiosto_edulliselle_ei_toimi_jos_kortilla_ei_tarpeeksi_rahaa(self):
        self.assertFalse(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_ei_riittava))
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa)

    def test_korttiosto_maukkaalle_ei_toimi_jos_kortilla_ei_tarpeeksi_rahaa(self):
        self.assertFalse(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_ei_riittava))
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, self.kassassa_rahaa)

    def test_kortille_rahaa_ladatessa_kortin_saldo_ja_kassan_rahamaara_muuttuvat_oikein(self):
        rahamaara = 500
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_tyhja, rahamaara)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), (self.kassassa_rahaa + rahamaara)/100)
        self.assertEqual(self.maksukortti_tyhja.saldo, rahamaara)

    def test_kortille_ei_voi_ladata_negatiivista_saldoa(self):
        rahamaara = -500
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti_tyhja, rahamaara)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), self.kassassa_rahaa/100)
        self.assertEqual(self.maksukortti_tyhja.saldo, 0)


