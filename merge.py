def merge_list(list1, list2):
    merged = list1 + list2
    for merged in merged.size() - 1:
        if merged[i] > merged[i + 1]:
            temp = merged[i]
            merged[i] = merged[i + 1]
            merged[i + 1] = temp 
    return merged