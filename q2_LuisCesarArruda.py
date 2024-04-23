# test_and_stress.py

import unittest
from unittest.mock import patch
import io

from q1_LuisCesarArruda import *

class TestTransaction(unittest.TestCase):

    def test_create_transaction_cash(self):
        mocked_receive_cash = lambda: None
        with patch('builtins.input', return_value='Dinheiro'), \
             patch('__main__.receive_cash', side_effect=mocked_receive_cash) as mocked_receive_cash:
            create_transaction()
            mocked_receive_cash.assert_called_once()

    def test_create_transaction_credit(self):
        mocked_request_account_details = lambda: None
        with patch('builtins.input', return_value='Crédito'), \
             patch('__main__.request_account_details', side_effect=mocked_request_account_details) as mocked_request_account_details:
            create_transaction()
            mocked_request_account_details.assert_called_once()

    def test_receive_cash(self):
        mocked_stdout = io.StringIO()
        with patch('builtins.input', return_value='Dinheiro'), \
             patch('sys.stdout', new=mocked_stdout):
            receive_cash()
            output = mocked_stdout.getvalue()
            print("Output:", output)
            self.assertIn("Imprimindo recibo de pagamento", output)

    def test_return_payment_receipt(self):
        mocked_stdout = io.StringIO()
        with patch('builtins.input', return_value='Dinheiro'), \
             patch('sys.stdout', new=mocked_stdout):
            return_payment_receipt()
            output = mocked_stdout.getvalue()
            print("Output:", output)
            self.assertIn("Devolvendo recibo de pagamento", output)

    def test_request_account_details(self):
        mocked_stdout = io.StringIO()
        with patch('builtins.input', return_value='123456'), \
             patch('sys.stdout', new=mocked_stdout):
            request_account_details()
            output = mocked_stdout.getvalue()
            print("Output:", output)
            self.assertIn("Solicitando pagamento do banco", output)

    def test_confirm_approval_from_bank(self):
        mocked_stdout = io.StringIO()
        with patch('sys.stdout', new=mocked_stdout):
            confirm_approval_from_bank()
            output = mocked_stdout.getvalue()
            print("Output:", output)
            self.assertIn("Confirmando aprovação do banco", output)

    def test_stress_transaction(self):
        num_transactions = 3
        stress_test = lambda _: [create_transaction() for _ in range(num_transactions)]
        stress_test(None)


if __name__ == '__main__':
    unittest.main()
