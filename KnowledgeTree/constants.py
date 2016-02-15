# Actual constant values

DEFAULT_INTEREST_RATE = 0.0675
MINIMUM_INTEREST_RATE = 0
MAXIMUM_INTEREST_RATE = 0.1
INTEREST_RATE_STEP = 0.0001

def interest_rate_num_steps():
    """Returns the number of steps in the interest rate range"""
    return int((MAXIMUM_INTEREST_RATE - MINIMUM_INTEREST_RATE)/INTEREST_RATE_STEP)
    
def interest_rate_range():
    """Generator function returning an iterator to the range of interest rate values"""
    val = MINIMUM_INTEREST_RATE
    while val <= MAXIMUM_INTEREST_RATE:
        yield val
        val += INTEREST_RATE_STEP

DEFAULT_INITIAL_BALANCE = 100000
MINIMUM_INITIAL_BALANCE = 0
MAXIMUM_INITIAL_BALANCE = 200000
INITIAL_BALANCE_STEP = 1000

def initial_balance_num_steps():
    """Returns the number of steps in the initial balance range"""
    return int((MAXIMUM_INITIAL_BALANCE - MINIMUM_INITIAL_BALANCE)/INITIAL_BALANCE_STEP)
    
def initial_balance_range():
    """Generator function returning an iterator to the range of initial balance values"""
    val = MINIMUM_INITIAL_BALANCE
    while val <= MAXIMUM_INITIAL_BALANCE:
        yield val
        val += INITIAL_BALANCE_STEP

MINIMUM_MONTHLY_PAYMENT = 0
MAXIMUM_MONTHLY_PAYMENT = 4000
MONTHLY_PAYMENT_STEP = 100

def monthly_payment_num_steps():
    """Returns the number of steps in the monthly payment range"""
    return int((MAXIMUM_MONTHLY_PAYMENT - MINIMUM_MONTHLY_PAYMENT)/MONTHLY_PAYMENT_STEP)
    
def monthly_payment_range():
    """Generator function returning an iterator to the range of monthly payment values"""
    val = MINIMUM_MONTHLY_PAYMENT
    while val <= MAXIMUM_MONTHLY_PAYMENT:
        yield val
        val += MONTHLY_PAYMENT_STEP

'''
# Values for testing the system
DEFAULT_INTEREST_RATE = 0.05
MINIMUM_INTEREST_RATE = 0
MAXIMUM_INTEREST_RATE = 0.1
INTEREST_RATE_STEP = 0.05
DEFAULT_INITIAL_BALANCE = 100000
MINIMUM_INITIAL_BALANCE = 0
MAXIMUM_INITIAL_BALANCE = 200000
INITIAL_BALANCE_STEP = 50000
MINIMUM_MONTHLY_PAYMENT = 0
MAXIMUM_MONTHLY_PAYMENT = 4000
MONTHLY_PAYMENT_STEP = 1000
'''

CANVAS_HEIGHT = 800
CANVAS_WIDTH = 800
canvas_dimensions = {
    'height': 800,
    'width': 800}
axes_display = {
    'display_height': 400,
    'display_width': 400,
    'corner_x': 100,
    'corner_y': 100,
    'x_label': 'Monthly payment ($)',
    'y_label': 'Time to payoff (yr)'}
axes_scale = {
    'x_min': 0,
    'x_max': 4000,
    'x_step': 500,
    'y_min': 0,
    'y_max': 30,
    'y_step': 5}

    



