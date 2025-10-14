def allcaps():
    def wrapper(func):
        string = func()
        return string.upper()
    return wrapper