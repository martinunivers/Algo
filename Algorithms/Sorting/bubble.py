"""
Bubble sorting algorithm that compares adjacent elements and swaps their positions
based on order condition (ascending or descending)
Optimized algorithm for the list already sorted, if no swap during the first loop, then the list is sorted
"""

def bubble(unsorted_list, sort):
   
    # Checking argument
    if (sort != "ASC" and sort != "DESC"):
        print("The argument passed to the sorting function is incorrect.")
        print("Please use ASC or DES as input")
        return unsorted_list
    elif (len(unsorted_list) == 0):
        print("The list passed to the sorting function is empty.")
        return unsorted_list
    list_len = len(unsorted_list)
    # Initialization
    swap = False

    # bubble sorting (Ascending)
    if (sort == "ASC"):
        for n in range(list_len - 1, 0, -1):
            for m in range(n):
                if (unsorted_list[m] > unsorted_list[m + 1]):
                    tmp = unsorted_list[m]
                    unsorted_list[m] = unsorted_list[m + 1]
                    unsorted_list[m + 1] = tmp
                    swap = True
            if not swap:
                break
    # bubble sorting (descending)
    else:
        for n in range(list_len - 1):
            for m in range(list_len - 1, n, -1):
                if (unsorted_list[m] > unsorted_list[m - 1]):
                    tmp = unsorted_list[m]
                    unsorted_list[m] = unsorted_list[m - 1]
                    unsorted_list[m - 1] = tmp
                    swap = True
            if not swap:
                break
    return unsorted_list