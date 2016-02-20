"""Database module for Loan Payoff Calculator

The times and interest rates are decimal values, stored to 4 decimal places of precision.
Internally, these values are multiplied by a conversion factor and stored as integers
"""

from peewee import *

DATABASE = SqliteDatabase('loan_payoff_data.db')


class DataPoint(Model):
    """Represents a single point of data that will be plotted"""
    Bo = IntegerField()
    r = IntegerField()
    p = IntegerField()
    t = IntegerField()
    
    class Meta:
        database = DATABASE


def initialize(database):
    """Initialize the database"""
    print("Initializing database")
    database.create_tables([DataPoint], safe=True)


def create_point(Bo, r, p, t):
    """Creates a DataPoint in the database with the given values"""
    with DATABASE.transaction():
        DataPoint.create(
            Bo=Bo,
            r=decimal_to_int(r),
            p=p,
            t=decimal_to_int(t))  


def delete_point(Bo, r, p, t):
    """Deletes a DataPoint from the database"""


def get_payoff_time(Bo, r, p):
    """Gets the payoff time associated with the given values of Bo, r, and p"""
    with DATABASE.transaction():
        try:
            point = DataPoint.get(DataPoint.Bo==Bo and DataPoint.r==decimal_to_int(r) and DataPoint.p==p)
            print("In database,", int_to_decimal(point.t))
            return int_to_decimal(point.t)
        except DoesNotExist:
            raise ValueError("No DataPoint was found with Bo={}, r={}, p={}".format(Bo, r, p))
        
    
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
    
    

    
    

