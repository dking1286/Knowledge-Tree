from peewee import *

DATABASE = SqliteDatabase('loan_payoff_data.db')

class DataPoint(Model):
    """Represents a single point of data that will be plotted"""
    Bo = IntegerField()
    r = DoubleField()
    p = IntegerField()
    t = DoubleField()
    
    class Meta:
        database = DATABASE
        
def initialize(database):
    """Initialize the database"""
    print("Initializing database")
    database.create_tables([DataPoint], safe=True)
