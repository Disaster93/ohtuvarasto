import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)



#

def test_init_negative_tilavuus_nollataan():
    v = Varasto(-5)
    assert v.tilavuus == 0

def test_init_negative_alkusaldo_nollataan():
    v = Varasto(10, -3)
    assert v.saldo == 0
    assert v.paljonko_mahtuu() == 10

def test_init_alkusaldo_yli_tilavuuden_katkaistaan():
    v = Varasto(10, 15)
    assert v.saldo == 10
    assert v.paljonko_mahtuu() == 0

def test_lisaa_varastoon_negatiivinen_ei_muuta():
    v = Varasto(10, 5)
    v.lisaa_varastoon(-2)
    assert v.saldo == 5
    assert v.paljonko_mahtuu() == 5

def test_lisaa_varastoon_yli_tilavuuden_tayttaa_katon():
    v = Varasto(10, 8)
    v.lisaa_varastoon(1000)
    assert v.saldo == 10
    assert v.paljonko_mahtuu() == 0

def test_ota_varastosta_negatiivinen_palauttaa_nolla_ei_muuta_saldoa():
    v = Varasto(10, 6)
    otettu = v.ota_varastosta(-3)
    assert otettu == 0
    assert v.saldo == 6

def test_ota_varastosta_yli_saldon_palauttaa_saldon_nollaa_varaston():
    v = Varasto(10, 6)
    otettu = v.ota_varastosta(1000)
    assert otettu == 6
    assert v.saldo == 0
    assert v.paljonko_mahtuu() == 10

def test_paljonko_mahtuu_vahenee_lisayksesta():
    v = Varasto(10)
    v.lisaa_varastoon(4)
    assert v.paljonko_mahtuu() == 6

def test_merkkijono_muoto():
    v = Varasto(10, 4.5)
    s = str(v)
    assert "saldo = 4.5" in s
    assert "vielä tilaa 5.5" in s
