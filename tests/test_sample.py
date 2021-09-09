from sample import increment

'''
### 1 ###

Our first test file.

Make sure:
    - You have __init__.py in your 'tests' folder
    - Your test function name starts by 'test_'
    - There's an assert in your test function
    - Run pytest from the parent directory

Now you can:
    - Call 'pytest' from the parent directory.

### Next: test_marked_sample.py ###
'''

def test_increment_number4():
    assert increment(4) == 5
