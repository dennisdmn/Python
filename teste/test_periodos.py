"""Testes das funcoes de manipulacao de periodos."""

import unittest

from python_operacional.periodos import periodo_anterior


class TestPeriodoAnterior(unittest.TestCase):
    def test_periodo_anterior_em_mes_comum(self) -> None:
        self.assertEqual(periodo_anterior("202607"), "202606")

    def test_periodo_anterior_na_virada_do_ano(self) -> None:
        self.assertEqual(periodo_anterior("202601"), "202512")

    def test_periodo_anterior_rejeita_entrada_invalida(self) -> None:
        entradas_invalidas = ("202613", "20260", "2026A1")

        for periodo_invalido in entradas_invalidas:
            with self.subTest(periodo=periodo_invalido):
                with self.assertRaises(ValueError):
                    periodo_anterior(periodo_invalido)


if __name__ == "__main__":
    unittest.main()
