from constants import *
from financial_tools import time_until_zero_balance, decimal_range
import database
from databse import DATABASE, database_action

class Model(object):
    """Contains the internal representations of the data to be displayed.
    
    Attributes:
        main (Main): A reference to the Main instance that contains the Model instance
        interest_rate (float): The current interest rate being displayed. This value will be matched
            to the interest_rate_slider in the Controller instance.
        payoff_times (dict<interest rate, list of points>): A dictionary that contains
            the data to be displayed. The keys are interest rates in decimal form, and the values
            are lists of points to be graphed. Each point's x value is a monthly payment,
            and the y value is the corresponding time to payoff, in years.
            
    Public methods:
        Model(main=None)
        
    Private methods:
        _calculate_payoff_times()
    """
    def __init__(self, main=None):
        if not main:
            raise ValueError()
            
        self.main = main
        self.interest_rate = DEFAULT_INTEREST_RATE
        self.initial_balance = DEFAULT_INITIAL_BALANCE
        self.payoff_times = dict()
    
    @database_action(DATABASE)
    def calculate_payoff_times(self):
        for Bo in range(MINIMUM_INITIAL_BALANCE, MAXIMUM_INITIAL_BALANCE, INITIAL_BALANCE_STEP):
            for r in decimal_range(MINIMUM_INTEREST_RATE, MAXIMUM_INTEREST_RATE, INTEREST_RATE_STEP):
                for p in range(MINIMUM_MONTHLY_PAYMENT, MAXIMUM_MONTHLY_PAYMENT, MONTHLY_PAYMENT_STEP):
                    print("Calculating for initial balance {0}, rate {1}, monthly payment {2}".format(Bo, r, p))
                    result = time_until_zero_balance(r, Bo, p)
                    if result is not None:
                        try:
                            database.DataPoint.create(
                                Bo=Bo,
                                r=r,
                                p=p,
                                t=result)
                        except database.IntegrityError:
                            pass
    
    @database_action(DATABASE)
    def load_payoff_times(self):
        data = database.DataPoint.select()
            for point in data:
                Bo, r, p, t = point.Bo, point.r, point.p, point.t
                self.payoff_times[Bo] = self.payoff_times.get(Bo, {})
                self.payoff_times[Bo][r] = self.payoff_times[Bo].get(r, {})
                self.payoff_times[Bo][r][p] = t

            