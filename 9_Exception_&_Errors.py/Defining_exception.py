# Defining our own exception

class ValueTooHighError(Exception):
    pass

def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
# value is too high

class ValueTooSmallError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value
    
def test_value(x):
    if x > 100:
        raise ValueTooHighError("value is too high")
    if x < 5:
        raise ValueTooSmallError("value is too small", x)

try:
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value)
# value is too small 1

