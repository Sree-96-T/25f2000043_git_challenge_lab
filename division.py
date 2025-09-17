def divide(a, b):
    """
    Return a / b if b != 0.
    If b is zero, return None to indicate error (handled by caller).
    """
    try:
        return a / b
    except ZeroDivisionError:
        return None
