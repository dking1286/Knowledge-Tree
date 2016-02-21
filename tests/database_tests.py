from nose.tools import *

import knowledge_tree.database as database
import knowledge_tree.constants as constants


def setup():
    pass


def teardown():
    pass


def test_database_conversion_functions():
    assert_equal(
        database.decimal_to_int(0.0675),
        675
    )
    assert_equal(
        database.int_to_decimal(675),
        0.0675
    )
    assert_equal(
        database.int_to_decimal(database.decimal_to_int(346)),
        346
    )


def test_get_payoff_time():
    pass
