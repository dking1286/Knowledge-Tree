"""Database module for Loan Payoff Calculator

The times and interest rates are decimal values, stored to 4 decimal places of precision.
Internally, these values are multiplied by a conversion factor and stored as integers
"""

import os.path

from peewee import *

import knowledge_tree.constants as constants

if constants.mode == 'actual':
    db_filename = 'loan_payoff_data_actual.db'
else:
    db_filename = 'loan_payoff_data_test.db'

db_directory = os.path.dirname(os.path.abspath(__file__))
db_full_path = os.path.join(db_directory, db_filename)

DATABASE = SqliteDatabase(db_full_path)


class DataPoint(Model):
    """Represents a single point of data that will be plotted"""
    id = IntegerField(primary_key=True, unique=True)
    Bo = IntegerField()
    r = IntegerField()
    p = IntegerField()
    t = IntegerField()
    
    class Meta:
        database = DATABASE
        order_by = ('id',)


def initialize(database):
    """Initialize the database"""
    print("Initializing database")
    database.create_tables([DataPoint], safe=True)


def create_point(id, Bo, r, p, t):
    """Creates a DataPoint in the database with the given values"""
    with DATABASE.transaction():
        DataPoint.create(
            id=id,
            Bo=Bo,
            r=decimal_to_int(r),
            p=p,
            t=decimal_to_int(t))


def get_payoff_time(Bo, r, p):
    """Gets the payoff time associated with the given values of Bo, r, and p

    Warning: This function performs a query to retrieve a *single* DataPoint, so don't use it to
        retrieve multiple. Instead, use get_time_vs_payment_data().
    """
    with DATABASE.transaction():
        try:
            query = DataPoint.select().where(
                DataPoint.Bo == Bo).where(
                DataPoint.r == decimal_to_int(r)).where(
                DataPoint.p == p)
            assert query.count() in (0, 1), "Number of points returned was {}".format(query.count())
            point = query.get()
            print("In database,", int_to_decimal(point.t))
            return int_to_decimal(point.t)
        except DoesNotExist:
            raise ValueError("No DataPoint was found with Bo={}, r={}, p={}".format(Bo, r, p))


def get_time_vs_payment_data(Bo, r):
    """Gets a list of time vs payment data from the database in a single query.

    Args:
        Bo (int): The initial balance of the account
        r (numeric): The interest rate on the account, in decimal form

    Returns a list of tuples, each of the form (monthly payment, payoff time)
    """
    result = []
    query = DataPoint.select().where(DataPoint.id << get_ids_for_time_vs_payment_data(Bo, r))
    for point in query:
        result.append((point.p, point.t))
    return result


def get_ids_for_time_vs_payment_data(Bo, r):
    """Calculates the ids of the DataPoints in the database that correspond to the given values of
    Bo and r.

    Args:
        Bo (int): The initial balance of the account
        r (numeric): The interest rate on the account, in decimal form
    """
    assert Bo in constants.initial_balance_range()
    assert r in constants.interest_rate_range()

    ids = []
    initial_id_val = 0
    initial_balance_id_jump_size = constants.monthly_payment_total_steps() * constants.interest_rate_total_steps()
    initial_balance_num_steps = get_num_steps(
        constants.initial_balance['min'],
        constants.initial_balance['max'],
        constants.initial_balance['step'],
        Bo
    )
    interest_rate_id_jump_size = constants.monthly_payment_total_steps()
    interest_rate_num_steps = get_num_steps(
        constants.interest_rate['min'],
        constants.interest_rate['max'],
        constants.interest_rate['step'],
        r
    )

    for _ in range(initial_balance_num_steps):
        initial_id_val += initial_balance_id_jump_size

    for _ in range(interest_rate_num_steps):
        initial_id_val += interest_rate_id_jump_size

    for id_ in range(initial_id_val, initial_id_val + constants.monthly_payment_total_steps()):
        ids.append(id_)

    return ids


def get_num_steps(start, stop, step, this):
    """Calculates how many steps into a process a given number is located

    Args:
        start: The start value of the process
        stop: The stop value of the process
        step: The step size of the process
        this: The number to test
    """
    if stop < start:
        raise ValueError('Start must be less than stop')
    if step > stop - start:
        raise ValueError('Step must be small enough that it fits between start and stop')

    result = 0
    for i in range(start, stop, step):
        if i >= this:
            return result
        result += 1
    raise ValueError('"This" must be between start and stop')


def decimal_to_int(number):
    """Converts a decimal number to the corresponding integer that will be used for internal storage"""
    return int(10000 * number)


def int_to_decimal(number):
    """Converts an integer in internal storage to the corresponding decimal value"""
    print("In int_to_decimal,", number)
    return float(number)/10000.0


def print_all_points():
    """Prints all of the points in the database"""
    with DATABASE.transaction():
        points = DataPoint.select()
        for point in points:
            print("(Bo, r, p, t) = ({}, {}, {}, {})".format(point.Bo, point.r, point.p, point.t))
