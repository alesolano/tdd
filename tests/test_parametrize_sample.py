import pytest
from sample import increment

'''
### 5 ###

pytest -v

### Next:  ###
'''

@pytest.mark.parametrize('integer', [1, 2])
def test_increment_integer(integer):
    assert increment(integer) == integer+1
