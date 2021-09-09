import pytest
from sample import increment

'''
### 4 ###


### Next:  ###
'''

@pytest.mark.xfail()
def test_increment_number4_fail():
    assert increment(4) == 3
