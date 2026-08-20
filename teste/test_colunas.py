"""Testes das funcoes de manipulacao de colunas."""

import unittest

import pandas as pd

from python_operacional.colunas import limpa_nomes_colunas


class TestLimpaNomesColunas(unittest.TestCase):
    def test_limpa_nomes_colunas(self) -> None:
        df = pd.DataFrame(columns=["  Razão Social  ", "Centro de Custo", "empresa"])

        resultado = limpa_nomes_colunas(df)

        self.assertIs(resultado, df)
        self.assertListEqual(
            resultado.columns.tolist(),
            ["razao_social", "centro_de_custo", "empresa"],
        )


if __name__ == "__main__":
    unittest.main()
