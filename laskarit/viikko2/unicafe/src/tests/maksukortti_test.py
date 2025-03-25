import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.0)

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(400)
        self.assertEqual(self.maksukortti.saldo_euroina(), 14.00)

    def test_saldo_vahenee_oiken_jos_rahaa_on_tarpeeksi(self):
        self.maksukortti.ota_rahaa(400)
        self.assertEqual(self.maksukortti.saldo_euroina(), 6.00)

    def test_saldo_ei_muutu_jos_rahaa_ei_ole_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)

    def test_ota_rahaa_palauttaa_true_jos_rahaa_on_tarpeeksi(self):
        self.assertTrue(self.maksukortti.ota_rahaa(400))
    
    def test_ota_rahaa_palauttaa_false_jos_rahaa_ei_ole_tarpeeksi(self):
        self.assertFalse(self.maksukortti.ota_rahaa(1100))

    def test_maksukortin_str_palauttaa_halutun_arvon(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")