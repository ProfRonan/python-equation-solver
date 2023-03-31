"""Esse arquivo testa o arquivo main.py"""

import importlib  # para importar o módulo main dinamicamente
import io  # para capturar a saída do print
import sys  # para restaurar o stdout padrão e remover o módulo main do cache
import unittest  # para criar o caso de teste
from unittest.mock import patch  # para simular a entrada do usuário


class TestMain(unittest.TestCase):
    """Classe que testa o arquivo main.py"""

    def setUp(self):
        """
        Inicializa o ambiente de teste removendo o módulo principal do cache.
        Isso é necessário para ser capaz de importá-lo novamente em cada teste.
        """
        sys.modules.pop("main", None)

    @patch("builtins.input", return_value="-1")
    def test_print_grau_m1(self, _mock_input):
        """Testa se o programa imprime "grau inválido" quando o usuário digita -1"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Grau inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "A equação é do segundo grau", captured_output.getvalue().strip()
        )
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())

    @patch("builtins.input", return_value="3")
    def test_print_grau_3(self, _mock_input):
        """Testa se o programa imprime "grau inválido" quando o usuário digita 3"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertIn("Grau inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "A equação é do segundo grau", captured_output.getvalue().strip()
        )
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "0"])
    def test_print_grau_1_a_0(self, _mock_input):
        """
        Testa se o programa imprime
        "A equação é do primeiro grau" e "Valor de a inválido"
        quando o usuário digita 1 e 0
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "A equação é do segundo grau", captured_output.getvalue().strip()
        )
        self.assertIn("Valor de a inválido", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "1", "0"])
    def test_print_grau_1_a_1_b_0(self, _mock_input):
        """
        Testa se o programa imprime "A equação é do primeiro grau" e "0.00"
        quando o usuário digita 1, 1 e 0.
        Ou seja, o programa deve resolver a raiz da equação 1x + 0 = 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "A equação é do segundo grau", captured_output.getvalue().strip()
        )
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())
        self.assertIn("0.00", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "1", "-10"])
    def test_print_grau_1_a_1_b_m10(self, _mock_input):
        """
        Testa se o programa imprime "A equação é do primeiro grau" e "10.00"
        quando o usuário digita 1, 1 e -10.
        Ou seja, o programa deve resolver a raiz da equação 1x - 10 = 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "A equação é do segundo grau", captured_output.getvalue().strip()
        )
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())
        self.assertIn("10.00", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["1", "2", "-5"])
    def test_print_grau_1_a_2_b_m5(self, _mock_input):
        """
        Testa se o programa imprime "A equação é do primeiro grau" e "2.50"
        quando o usuário digita 1, 2 e -5.
        Ou seja, o programa deve resolver a raiz da equação 2x - 5 = 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertNotIn(
            "A equação é do segundo grau", captured_output.getvalue().strip()
        )
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())
        self.assertIn("2.50", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["2", "0"])
    def test_print_grau_2_a_0(self, _mock_input):
        """
        Testa se o programa imprime
        "A equação é do segundo grau" e "Valor de a inválido"
        quando o usuário digita 2 e 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertIn("A equação é do segundo grau", captured_output.getvalue().strip())
        self.assertIn("Valor de a inválido", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["2", "1", "0", "0"])
    def test_print_grau_2_a_1_b_0_c_0(self, _mock_input):
        """
        Testa se o programa imprime "A equação é do segundo grau",
        "A equação possui uma raiz real" e "0.00"
        quando o usuário digita 2, 1, 0, 0.
        Ou seja, o programa deve resolver a raiz da equação 1x² + 0x + 0 = 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertIn("A equação é do segundo grau", captured_output.getvalue().strip())
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())
        self.assertIn(
            "A equação possui uma raiz real", captured_output.getvalue().strip()
        )
        self.assertIn("0.00", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["2", "3", "0", "-27"])
    def test_print_grau_2_a_1_b_0_c_m27(self, _mock_input):
        """
        Testa se o programa imprime "A equação é do segundo grau",
        "A equação possui uma raiz real", "-3.00" e "3.00"
        quando o usuário digita 2, 3, 0, 27.
        Ou seja, o programa deve resolver a raiz da equação 3x² + 0x - 27 = 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertIn("A equação é do segundo grau", captured_output.getvalue().strip())
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())
        self.assertIn(
            "A equação possui duas raízes reais", captured_output.getvalue().strip()
        )
        self.assertIn("-3.00", captured_output.getvalue().strip())
        self.assertIn("3.00", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["2", "1", "-1", "-12"])
    def test_print_grau_2_a_1_b_m1_c_m12(self, _mock_input):
        """
        Testa se o programa imprime "A equação é do segundo grau",
        "A equação possui uma raiz real", "-3.00" e "4.00"
        quando o usuário digita 2, 1, -1, -12.
        Ou seja, o programa deve resolver a raiz da equação 1x² - 1x - 12 = 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertIn("A equação é do segundo grau", captured_output.getvalue().strip())
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())
        self.assertIn(
            "A equação possui duas raízes reais", captured_output.getvalue().strip()
        )
        self.assertIn("-3.00", captured_output.getvalue().strip())
        self.assertIn("4.00", captured_output.getvalue().strip())

    @patch("builtins.input", side_effect=["2", "1", "0", "10"])
    def test_print_grau_2_a_1_b_0_c_10(self, _mock_input):
        """
        Testa se o programa imprime "A equação é do segundo grau" e
        "A equação não possui raízes reais" quando o usuário digita 2, 1, 0, 10.
        Ou seja, o programa deve resolver a raiz da equação 1x² + 0x + 10 = 0.
        """
        captured_output = io.StringIO()
        sys.stdout = captured_output
        importlib.import_module("main")
        sys.stdout = sys.__stdout__
        self.assertNotIn("Grau inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação é do primeiro grau", captured_output.getvalue().strip()
        )
        self.assertIn("A equação é do segundo grau", captured_output.getvalue().strip())
        self.assertNotIn("Valor de a inválido", captured_output.getvalue().strip())
        self.assertNotIn(
            "A equação possui duas raízes reais", captured_output.getvalue().strip()
        )
        self.assertIn(
            "A equação não possui raízes reais", captured_output.getvalue().strip()
        )
