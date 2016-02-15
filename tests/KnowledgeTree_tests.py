from nose.tools import *

import KnowledgeTree.database as db

def setup():
    print("SETUP!")
    
def teardown():
    print("TEAR DOWN!")
    
def test_database_functions():
    assert_equal(
        db.decimal_to_int(0.0675),
        675)
    assert_equal(
        db.int_to_decimal(675),
        0.0675)
    
