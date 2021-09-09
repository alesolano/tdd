import pytest
from sample import decrement

'''
### 2 ###

We can add marks to our tests so we just evaluate a particular group of tests.

Make sure:
    - You import pytest
    - You have the marker described in pytest.ini

Now you can:
    - Call 'pytest -m decrement' to see that only this test is run

### Next: ... ###
'''

@pytest.mark.decrement
def test_decrement_number6():
    assert decrement(6) == 5
