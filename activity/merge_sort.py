from .mergelib import merge_sorted

# Implement merge_sort
# merge_sorted is a helper function that merges 2
# already sorted lists in linear time and space
# with respect to the combined lengths of the lists.

def merge_sort(data):
    # base
    if len(data) <= 1: 
        return list(data)

    mid = len(data)//2

    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])


    return merge_sorted(left, right)