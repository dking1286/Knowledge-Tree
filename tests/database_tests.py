from nose.tools import *

import knowledge_tree.database as db


def setup():
    pass


def teardown():
    pass


def test_database_conversion_functions():
    assert_equal(
        db.decimal_to_int(0.0675),
        675)
    assert_equal(
        db.int_to_decimal(675),
        0.0675)


def test_get_payoff_time():
    pass
