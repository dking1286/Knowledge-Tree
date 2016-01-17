from constants import (DEFAULT_INTEREST_RATE, MINIMUM_INTEREST_RATE, MAXIMUM_INTEREST_RATE,
                       DEFAULT_INITIAL_BALANCE, MINIMUM_INITIAL_BALANCE,
                       MAXIMUM_INITIAL_BALANCE, INITIAL_BALANCE_STEP, INTEREST_RATE_STEP)
from financial_tools import generate_years_vs_payment_data, decimal_range

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
        
    def calculate_payoff_times(self):
        bar_val = 0
        for Bo in range(MINIMUM_INITIAL_BALANCE, MAXIMUM_INITIAL_BALANCE, INITIAL_BALANCE_STEP):
            for r in decimal_range(MINIMUM_INTEREST_RATE, MAXIMUM_INTEREST_RATE, INTEREST_RATE_STEP):
                print("Initial balance is {0}, rate is {1}".format(Bo, r))
                print("Progress bar value is {0}".format(bar_val))
                self.payoff_times[(r, Bo)] = generate_years_vs_payment_data(r, Bo)
                bar_val += 1
                self.main.view.progress_bar.update(bar_val)
            