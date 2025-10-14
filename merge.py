def sort_list(arr: list):
    for i in range(0, len(arr)):
        for j in range(1, len(arr) - i):
            if arr[j-1] > arr[j]:
                temp = arr[j-1]
                arr[j-1] = arr[j]
                arr[j] = temp

def merge_list(a: list, b: list) -> list:
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("Input must be a list")
    merged = a + b
    sort_list(merged)
    return merged