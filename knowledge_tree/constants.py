"""Constant values for Knowledge Tree"""

mode = 'test'
interest_rate = {}
initial_balance = {}
monthly_payment = {}


def set_mode(new_mode):
    global mode
    mode = new_mode

    if mode == 'actual':
        interest_rate['default'] = 0.0675
        interest_rate['min'] = 0
        interest_rate['max'] = 0.1
        interest_rate['step'] = 0.0001

        initial_balance['default'] = 100000
        initial_balance['min'] = 0
        initial_balance['max'] = 200000
        initial_balance['step'] = 1000

        monthly_payment['min'] = 0
        monthly_payment['max'] = 4000
        monthly_payment['step'] = 100

    elif mode == 'test':
        interest_rate['default'] = 0.05
        interest_rate['min'] = 0
        interest_rate['max'] = 0.1
        interest_rate['step'] = 0.01

        initial_balance['default'] = 100000
        initial_balance['min'] = 0
        initial_balance['max'] = 200000
        initial_balance['step'] = 50000

        monthly_payment['min'] = 0
        monthly_payment['max'] = 4000
        monthly_payment['step'] = 1000
    else:
        raise ValueError()


def interest_rate_total_steps():
    """Returns the number of steps in the interest rate range"""
    return int((interest_rate['max'] - interest_rate['min'])/interest_rate['step'])


def interest_rate_range():
    """Generator function returning an iterator to the range of interest rate values"""
    val = interest_rate['min']
    while val <= interest_rate['max']:
        yield val
        val += interest_rate['step']


def initial_balance_total_steps():
    """Returns the number of steps in the initial balance range"""
    return int((initial_balance['max'] - initial_balance['min'])/initial_balance['step'])


def initial_balance_range():
    """Generator function returning an iterator to the range of initial balance values"""
    val = initial_balance['min']
    while val <= initial_balance['max']:
        yield val
        val += initial_balance['step']


def monthly_payment_total_steps():
    """Returns the number of steps in the monthly payment range"""
    return int((monthly_payment['max'] - monthly_payment['min'])/monthly_payment['step'])


def monthly_payment_range():
    """Generator function returning an iterator to the range of monthly payment values"""
    val = monthly_payment['min']
    while val <= monthly_payment['max']:
        yield val
        val += monthly_payment['step']

canvas_dimensions = {
    'height': 800,
    'width': 800}
axes_display = {
    'display_height': 400,
    'display_width': 400,
    'corner_x': 100,
    'corner_y': 600,
    'x_label': 'Monthly payment ($)',
    'y_label': 'Time to payoff (yr)'}
axes_scale = {
    'x_min': 0,
    'x_max': 4000,
    'x_step': 500,
    'y_min': 0,
    'y_max': 30,
    'y_step': 5}

set_mode(mode)