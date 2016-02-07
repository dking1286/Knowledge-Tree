# Actual constant values

DEFAULT_INTEREST_RATE = 0.0675
MINIMUM_INTEREST_RATE = 0
MAXIMUM_INTEREST_RATE = 0.1
INTEREST_RATE_STEP = 0.0001
def interest_rate_range():
    val = MINIMUM_INTEREST_RATE
    while val <= MAXIMUM_INTEREST_RATE:
        yield val
        val += INTEREST_RATE_STEP

DEFAULT_INITIAL_BALANCE = 100000
MINIMUM_INITIAL_BALANCE = 0
MAXIMUM_INITIAL_BALANCE = 200000
INITIAL_BALANCE_STEP = 1000
def initial_balance_range():
    val = MINIMUM_INITIAL_BALANCE
    while val <= MAXIMUM_INITIAL_BALANCE:
        yield val
        val += INITIAL_BALANCE_STEP

MINIMUM_MONTHLY_PAYMENT = 0
MAXIMUM_MONTHLY_PAYMENT = 4000
MONTHLY_PAYMENT_STEP = 100
def monthly_payment_range():
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
    'y_step'; 5}

    



