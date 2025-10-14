def allcaps(func):
    def wrapper():
        string = func()
        upperCase = string.upper()
        return upperCase
    return wrapper