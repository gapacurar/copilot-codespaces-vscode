import unittest
from BankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        self.account1 = BankAccount("123456", "John Doe", 1000.0)
        self.account2 = BankAccount("654321", "Jane Doe", 500.0)

    def test_initial_balance(self):
        self.assertEqual(self.account1.get_balance(), 1000.0)
        self.assertEqual(self.account2.get_balance(), 500.0)

    def test_deposit_positive_amount(self):
        self.assertTrue(self.account1.deposit(200.0))
        self.assertEqual(self.account1.get_balance(), 1200.0)

    def test_deposit_negative_amount(self):
        self.assertFalse(self.account1.deposit(-200.0))
        self.assertEqual(self.account1.get_balance(), 1000.0)

    def test_withdraw_valid_amount(self):
        self.assertTrue(self.account1.withdraw(300.0))
        self.assertEqual(self.account1.get_balance(), 700.0)

    def test_withdraw_invalid_amount(self):
        self.assertFalse(self.account1.withdraw(1500.0))
        self.assertEqual(self.account1.get_balance(), 1000.0)

    def test_withdraw_negative_amount(self):
        self.assertFalse(self.account1.withdraw(-100.0))
        self.assertEqual(self.account1.get_balance(), 1000.0)

    def test_transfer_valid_amount(self):
        self.assertTrue(self.account1.transfer(200.0, self.account2))
        self.assertEqual(self.account1.get_balance(), 800.0)
        self.assertEqual(self.account2.get_balance(), 700.0)

    def test_transfer_invalid_amount(self):
        self.assertFalse(self.account1.transfer(1500.0, self.account2))
        self.assertEqual(self.account1.get_balance(), 1000.0)
        self.assertEqual(self.account2.get_balance(), 500.0)

    def test_transfer_negative_amount(self):
        self.assertFalse(self.account1.transfer(-100.0, self.account2))
        self.assertEqual(self.account1.get_balance(), 1000.0)
        self.assertEqual(self.account2.get_balance(), 500.0)

    def test_str_method(self):
        self.assertEqual(str(self.account1), "Account(123456, John Doe, Balance: 1000.0)")
        self.assertEqual(str(self.account2), "Account(654321, Jane Doe, Balance: 500.0)")

    def test_credit_positive_amount(self):
        self.assertTrue(self.account1.credit(300.0))
        self.assertEqual(self.account1.get_balance(), 1300.0)

    def test_credit_negative_amount(self):
        self.assertFalse(self.account1.credit(-300.0))
        self.assertEqual(self.account1.get_balance(), 1000.0)

    def test_debit_valid_amount(self):
        self.assertTrue(self.account1.debit(200.0))
        self.assertEqual(self.account1.get_balance(), 800.0)

    def test_debit_invalid_amount(self):
        self.assertFalse(self.account1.debit(1500.0))
        self.assertEqual(self.account1.get_balance(), 1000.0)

    def test_debit_negative_amount(self):
        self.assertFalse(self.account1.debit(-200.0))
        self.assertEqual(self.account1.get_balance(), 1000.0)

if __name__ == "__main__":
    unittest.main(exit=False)