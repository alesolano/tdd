import pytest
from sample import decrement

'''
### 3 ###


Now you can:
    - pytest -m 'decrement'
    - pytest -m 'decrement and not float'

'''

@pytest.mark.decrement
@pytest.mark.float
def test_decrement_number3_1416():
    assert decrement(3.1416) == 2.1416
