import unittest

from model import Model
import database
import financial_tools as ft

DB = database.SqliteDatabase("test.db")


class ModelCalculationTest(unittest.TestCase):
    def setUp(self):
        self.model = test_model

    def test_no_interest(self):
        self.assertEqual(
            4.17,
            round(self.model.get_payoff_time(Bo=50000, r=0, p=1000), 2))
    
    def test_no_interest_ft_to_db(self):
        data_point = database.DataPoint.get(
            database.DataPoint.Bo == 50000,
            database.DataPoint.r == 0,
            database.DataPoint.p == 1000)
        self.assertEqual(
            round(ft.time_until_zero_balance(0, 50000, 1000), 2),
            round(data_point.t, 2))

    def test_no_interest_ft_to_dict(self):
        self.assertEqual(
            round(ft.time_until_zero_balance(0, 50000, 1000), 2),
            round(self.model.get_payoff_time(Bo=50000, r=0, p=1000), 2))
    
    def test_with_interest_ft_to_db(self):
        data_point = database.DataPoint.get(
            database.DataPoint.Bo == 50000,
            database.DataPoint.r == 0.05,
            database.DataPoint.p == 1000)
        self.assertEqual(
            round(ft.time_until_zero_balance(0.05, 50000, 1000), 2),
            round(data_point.t, 2))
        
    def test_with_interest_ft_to_dict(self):
        self.assertEqual(
            round(ft.time_until_zero_balance(0.05, 50000, 1000), 2), 
            round(self.model.get_payoff_time(Bo=50000, r=0.05, p=1000), 2))
        
if __name__ == '__main__':
    database.initialize(DB)
    test_model = Model(db=DB)
    test_model.calculate_payoff_times()
    test_model.load_payoff_times()
    unittest.main()