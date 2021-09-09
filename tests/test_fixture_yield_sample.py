import pytest
from sample import increment, Database

'''
### 7 ###




### Next:  ###
'''

@pytest.fixture()
def data_from_database():
    db = Database()
    db.connect()
    yield db.get_data()
    db.disconnect()

def test_increment_db(data_from_database):
    for integer in data_from_database:
        assert increment(integer) == integer+1

