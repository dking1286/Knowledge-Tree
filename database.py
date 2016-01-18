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
        
def database_action(database):
    """Decorator indicating that the function requires the usage of the database.
    
    The given database is opened before the decorated function is executed and closed
    when the function is finished.
    """
    def decorator(func):
        def new_behavior(*args, **kwargs):
            database.connect()
            result = func(*args, **kwargs)
            database.close()
            return result
        return new_behavior
    return decorator