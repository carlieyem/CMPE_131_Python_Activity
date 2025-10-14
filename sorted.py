def sort_dic(dictionary):
    for i in range(0, len(dictionary)):
        for j in range(1, len(dictionary) - i):
            if dictionary[j-1][0] < dictionary[j][0]:
                temp = dictionary[j-1]
                dictionary[j-1] = dictionary[j]
                dictionary[j] = temp
    return dictionary

def reverse_sort_dictionary(dictionary):
    sorted_dict = []
    
    for key in dictionary:
        tupleValue = dictionary[key]
        sorted_dict.append((key, tupleValue[0]))

    sorted_dict = sort_dic(sorted_dict)
    return sorted_dict