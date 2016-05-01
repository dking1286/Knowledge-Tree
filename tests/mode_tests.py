from nose.tools import *

import knowledge_tree.constants as constants


def test_set_mode():
    constants.set_mode('test')
    assert_not_in(1000, constants.initial_balance_range())

    constants.set_mode('actual')
    assert_in(1000, constants.initial_balance_range())
