def quick_sort(alist):
    """
    Input: unsorted list of integers
    Returns sorted list of integers using Quicksort
    """
    if len(alist) < 2:
        return alist
    else:
        pivot = alist[-1]
        smaller, equal, larger = [],[],[]
        for num in alist:
            if num < pivot:
                smaller.append(num)
            elif num == pivot:
                equal.append(num)
            else:
                larger.append(num)
        return quick_sort(smaller) + equal + quick_sort(larger)


l =[6,8,1,4,10,7,8,9,3,2,5]
print(quick_sort(l))