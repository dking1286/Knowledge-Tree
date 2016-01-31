import constants
from financial_tools import time_until_zero_balance, decimal_range
import database

class Model(object):
    """Contains the internal representations of the data to be displayed.
    
    Attributes:
        main (Main): A reference to the Main instance that contains the Model instance
        database (peewee database): A reference to the database the Model instance will
            read and write from
        interest_rate (float): The current interest rate being displayed. This value will be matched
            to the interest_rate_slider in the Controller instance.
        initial_balance (int): The current initial balance being displayed. This value will
            be matched to the initial_balance_slider in the Controller instance.
        payoff_times (dict<initial balance, dict<interest rate, dict<payment, payoff time>>>):
            A nested dictionary structure containing the data to be plotted.
            
    Public methods:
        Model(main=None)
        calculate_payoff_times()
    """
    def __init__(self, main=None, db=None):    
        self.main = main
        self.database = db
        self.interest_rate = constants.DEFAULT_INTEREST_RATE
        self.initial_balance = constants.DEFAULT_INITIAL_BALANCE
        self.payoff_times = dict()
    
    def calculate_payoff_times(self):
        with self.database.transaction():
            for Bo in constants.initial_balance_range():
                for r in constants.interest_rate_range():
                    for p in constants.monthly_payment_range():
                        print("Calculating for initial balance {0}, rate {1}, monthly payment {2}".format(Bo, r, p))
                        result = time_until_zero_balance(r, Bo, p)
                        if result is not None:
                            database.DataPoint.create(
                                Bo=Bo,
                                r=r,
                                p=p,
                                t=result)
    
    def load_payoff_times(self):
        with self.database.transaction():
            data = database.DataPoint.select()
            for point in data:
                Bo, r, p, t = point.Bo, point.r, point.p, point.t
                self.payoff_times[Bo] = self.payoff_times.get(Bo, {})
                self.payoff_times[Bo][r] = self.payoff_times[Bo].get(r, {})
                self.payoff_times[Bo][r][p] = t
    
    def get_payoff_time(self, Bo=0, r=0, p=0):
        return self.payoff_times[Bo][r][p]

            