from peewee import *

DATABASE = SqliteDatabase('loan_payoff_data.db')

class DataPoint(Model):
    initial_balance = IntegerField()
    interest_rate = DoubleField()
    monthly_deposit = IntegerField()
    payoff_time = Double_Field()
    
    class Meta:
        databse = DATABASE
        
def initialize():
    """Initialize the database"""
    DATABASE.create_tables([DataPoint], safe=True)
        
def database_action(database):
    def decorator(func):
        def new_behavior():
            database.connect()
            result = func()
            database.close()
            return result
        return new_behavior
    return decorator