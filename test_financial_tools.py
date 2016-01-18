import unittest

import financial_tools as ft

class CalculateAccountBalanceTests(unittest.TestCase):
    def test_no_payment(self):
        self.assertEqual(121, round(ft.calculate_account_balance(t=2, r=0.1, Bo=100, p=0), 2))
        
    def test_investment_with_payment(self):
        self.assertEqual(142, round(ft.calculate_account_balance(t=2, r=0.1, Bo=100, p=10), 2))
        
    def test_debt_with_payment(self):
        self.assertEqual(89.5, round(ft.calculate_account_balance(t=2, r=0.1, Bo=100, p=-15), 2))
    
    
    
class AccountBalanceTests(unittest.TestCase):
    def test_monthly_compunding_greater_than_yearly(self):
        self.assertGreater(round(ft.account_balance(t=10, r=0.1, Bo=1000, p=0, compounding='monthly'), 2),
                           round(ft.account_balance(t=10, r=0.1, Bo=1000, p=0, compounding='yearly'), 2))
                           
    def test_no_interest(self):
        self.assertEqual(1000, ft.account_balance(t=1, r=0, Bo=13000, p=-1000))

class TimeUntilZeroBalanceTests(unittest.TestCase):
    def test_time_until_zero_balance_no_interest(self):
        self.assertEqual(5, round(ft.time_until_zero_balance(0, 60000, 1000)))
    
    def test_recursion_depth_reached(self):
        self.assertEqual(4.17, round(ft.time_until_zero_balance(0, 50000, 1000), 2))

if __name__ == '__main__':
    unittest.main()