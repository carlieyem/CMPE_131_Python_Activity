def cacti_number(plot: list) -> int:
    plantable = 0
    if not isinstance(plot, list):
        raise TypeError("Input must be a list")
    for row in plot:
        for number in row:
            if plot[row][number] == 0 and plot[row-1][number] != 1 and plot[row+1][number] != 1 and plot[row][number-1] != 1 and plot[row][number+1] != 1:
                plantable += 1

    return plantable