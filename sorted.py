def reverse_sort_dictionary(dictionary):
    sorted_dict = sorted(dictionary.items(), key=lambda item: item[0], reverse = True)
    return [(name, number[0] for name, data in sorted_dict)]