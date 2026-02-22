from django.test import TestCase


class ExemploTest(TestCase):
    """
    Docstring para ExemploTest
    """

    def teste_soma_simples(self):
        soma = 1 + 1

        self.assertEqual(soma, 2)
