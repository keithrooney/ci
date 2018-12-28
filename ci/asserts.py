

def is_true(condition, message="Expected condition to evaluate to True, actually evaluated to False."):
    if condition:
        raise AssertionError(message)


def is_equal(value, other, message="Expected values to equal each other, neither are equal to the other."):
    is_true(value != other, message)
