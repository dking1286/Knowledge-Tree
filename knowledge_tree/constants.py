"""Constant values for Knowledge Tree"""

initial_balance = {
    'default': 100000,
    'min': 0,
    'max': 200000,
    'step': 1000
}
interest_rate = {
    'default': 0.0675,
    'min': 0,
    'max': 0.1,
    'step': 0.0001
}
monthly_payment = {
    'min': 0,
    'max': 4000,
    'step': 100
}
canvas_dimensions = {
    'height': 800,
    'width': 800
}
axes_display = {
    'display_height': 400,
    'display_width': 400,
    'corner_x': 100,
    'corner_y': 600,
    'x_label': 'Monthly payment ($)',
    'y_label': 'Time to payoff (yr)'
}
axes_scale = {
    'x_min': 0,
    'x_max': 4000,
    'x_step': 500,
    'y_min': 0,
    'y_max': 30,
    'y_step': 5
}
initial_balance_slider_data = {
    'x': 100,
    'y': 700,
    'scale_min': initial_balance['min'],
    'scale_max': initial_balance['max'],
    'resolution': initial_balance['step'],
    'label': "Initial balance ($)"
}
interest_rate_slider_data = {
    'x': 500,
    'y': 700,
    'scale_min': interest_rate['min'],
    'scale_max': interest_rate['max'],
    'resolution': interest_rate['step'],
    'label': "APR"
}


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



