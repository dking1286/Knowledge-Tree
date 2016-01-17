from point import Point
from constants import MINIMUM_MONTHLY_PAYMENT, MAXIMUM_MONTHLY_PAYMENT

def generate_years_vs_payment_data(r, Bo):
    results = list()
    for p in range(MINIMUM_MONTHLY_PAYMENT, MAXIMUM_MONTHLY_PAYMENT):
        results.append(Point(p, time_until_zero_balance(r, Bo, p)))
    return results

def time_until_zero_balance(r, Bo, p):
    """Calculates the time in years until a loan account will have zero balance
    
    Args:
        r (float): Yearly interest rate in decimal format
        Bo (int): Initial balance on the account
        p (int): Monthly payment on the account
    """
        
    t = 0
    if account_balance(t=0, r=r, Bo=Bo, p=-p) <= account_balance(t=1, r=r, Bo=Bo, p=-p):
        return None
    while account_balance(t=t, r=r, Bo=Bo, p=-p) > 0:
        t += 1
    while account_balance(t=t, r=r, Bo=Bo, p=-p) < 0:
        t -= 0.1
    while account_balance(t=t, r=r, Bo=Bo, p=-p) > 0:
        t += 0.01
    return t

def account_balance(t=0, r=0, Bo=0, p=0, compounding='monthly'):
    """Returns the balance of an account at time t.
    
    Args:
        t (numeric): The time in years
        r (float): The yearly interest rate on the account
        Bo (numeric): The initial balance of the account
        p (numeric): The payment into the account per month. This may be positive,
            to indicate a deposit, or negative to indicate a deduction (such as
            making a payment on a loan)
        compounding (str): May be either 'yearly' or 'monthly'
    """
    if compounding=='monthly':
        params = {'t': 12 * t,
                  'r': yearly_to_monthly_interest_rate(r),
                  'Bo': Bo,
                  'p': p}
    elif compounding=='yearly':
        params = {'t': t,
                  'r': r,
                  'Bo': Bo,
                  'p': 12 * p}
    else:
        raise ValueError('compounding must be monthly or yearly')
    return calculate_account_balance(**params)

def calculate_account_balance(t=0, r=0, Bo=0, p=0):
    """Returns the remaining balance of a loan at time t, given an interest rate r, initial
    balance Bo, and payment per unit time p. t, r, and p may be either monthly or yearly,
    but they must all be compatible.
    
    This may be used to calculate either a growing account, like an investment, or
    a shrinking account, like a debt. In the case of a debt, p should be negative to
    indicate that the payment is *deducted* from the account balance.
    
    Args:
        t (numeric): The time in either months or years
        r (float): The interest rate per unit time
        Bo (numeric): The initial balance of the account
        p (numeric): The payment per unit time on the account
    """
    if t:
        return calculate_account_balance(t-1, r, Bo, p)*(1 + r) + p
    else:
        return Bo

def yearly_to_monthly_interest_rate(rate):
    """Converts a yearly interest rate to a monthly interest rate
    
    Args:
        rate (float): The yearly interest rate in decimal format
    """
    return (1 + rate)**(1.0/12) - 1
    
def decimal_range(start, stop, step):
    next_val = start
    while next_val < stop:
        yield next_val
        next_val += step
    
