def my_steps(n: int) -> int:
    if not isinstance(n, int) or (n not in range(1, 25)):
        raise TypeError("Input must be an integer")
    
    if n <= 2:
        return n
    for i in range(3, n+1):
        return my_steps(n-1) + my_steps(n-2)