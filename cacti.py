def cacti_number(plot):
    plantable = 0
    for row in plot:
        for number in row:
            if plot[row][number] == 0 and plot[row-1][number] != 1 and plot[row+1][number] != 1 and plot[row][number-1] != 1 and plot[row][number+1] != 1:
                plantable += 1

    return plantable