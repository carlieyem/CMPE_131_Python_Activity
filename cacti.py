def cacti_number(plot: list) -> int:
    plantable = 0
    if not isinstance(plot, list):
        raise TypeError("Input must be a list")
    
    plotLen = len(plot)
    for y in range(0, plotLen):
        rowLen = len(plot[y])
        for x in rowLen:
            if plot[y][x] == 0 and plot[y-1][x] != 1 and plot[y+1][x] != 1 and plot[y][x-1] != 1 and plot[y][x+1] != 1:
                plantable += 1

    return plantable