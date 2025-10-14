def my_steps(n):
    if (n < 1) or (n >25):
        return 0, "ValueError"
    a = 1
    b = 2
    for i in range(3, n+1):
        if i == 1:
            return 1
        if i == 2:
            return 2
        else:
            return my_steps(n-1) + my_steps(n-2)