

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
    """Returns the balance of a loan, given a 
    starting balance, yearly interest rate, and yearly
    payment. 
    
    Args:
        t (float): The time in years
        r (float): The yearly interest rate in decimal form
        Bo (float): The starting balance of the loan
        P (float): The yearly payment on the loan, or monthly payment if
            compunding is set to 'monthly'
        compounding (string): Can be either 'yearly' or 'monthly'
    """
    if r:
        return Bo*(1 + r)**t + p*(float(1 - (1 + r)**t)/(-r))
    else:
        return Bo*(1 + r)**t + p*t

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
    
