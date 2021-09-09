

def increment(x):
    '''
    Increments variable by one
    '''
    return x + 1



def decrement(x):
    '''
    Decrement variable by one
    '''
    return x - 1


class Database():

    def __init__(self):
        self.data = [1, 2, 3]
        self.connected = False
    
    def connect(self):
        self.connected = True

    def get_data(self):
        assert self.connected
        return self.data

    def disconnect(self):
        self.connected = False
