from nose.tools import *

import knowledge_tree.database as database
import knowledge_tree.constants as constants


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


def test_get_num_steps():
    assert_equal(
        database.get_num_steps(0, 10, 1, 3),
        3,
        "basic test failed"
    )
    assert_equal(
        database.get_num_steps(10, 30, 5, 20),
        2,
        "second test failed"
    )
    assert_equal(
        database.get_num_steps(
            constants.initial_balance['min'],
            constants.initial_balance['max'],
            constants.initial_balance['step'],
            constants.initial_balance['min'] + 2*constants.initial_balance['step']
        ),
        2,
        "test with actual values from knowledge_tree constants failed"
    )
    assert_raises(
        ValueError,
        database.get_num_steps,
        5, 0, 1, 1
    )
    assert_raises(
        ValueError,
        database.get_num_steps,
        0, 5, 10, 4
    )
    assert_raises(
        ValueError,
        database.get_num_steps,
        0, 5, 1, 10
    )


def test_get_ids_for_time_vs_payment_data():
    pass
