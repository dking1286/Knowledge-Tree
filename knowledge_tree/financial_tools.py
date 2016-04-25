import math


def payments_to_payoff(a, i, p):
    """Returns the number of payments required to reach zero balance on a loan

    Args:
        a: The initial loan balance
        i: The interest rate per payment period (NOT per year)
        p: The payment per payment period

    Raises:
        AssertionError: Raised in the event that any of the three arguments are non-numeric
    """
    assert type(a) == int or type(a) == float, "type of a is {}".format(type(a))
    assert type(i) == int or type(i) == float, "type of i is {}".format(type(i))
    assert type(p) == int or type(p) == float, "type of p is {}".format(type(p))

    if p == 0:
        print("p is 0")
        return None

    try:
        numerator = -math.log(1 - i * a / p)
        denominator = math.log(1 + i)
        result = numerator / denominator
        print("payments_to_payoff({}, {}, {}) => {}".format(a, i, p, result))
        return result
    except ValueError:
        print("payments_to_payoff({}, {}, {}) => Log domain error".format(a, i, p))
        return None


def decimal_range(start, stop, step):
    next_val = start
    while next_val < stop:
        yield next_val
        next_val += step

