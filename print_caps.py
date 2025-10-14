def allcaps():
    def wrapper(func):
        string = func()
        upperCase = string.upper()
        return upperCase
    return wrapper