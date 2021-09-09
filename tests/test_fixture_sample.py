import pytest
from sample import increment

'''
### 6 ###

Fixtures are functions that are run by pytest before
(and sometimes after) the actual test functions.
You can use fixtures to get a data set for the tests to work on



### Next:  ###
'''

@pytest.fixture()
def number_8():
    '''
    Prepare data
    '''
    return 8


def test_increment_integer(number_8):
    assert increment(number_8) == 9
