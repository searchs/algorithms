def selection_sort_ola(arr):
    # O(n2)
    marker = 0

    while marker < len(arr):
        for num in range(marker, len(arr)):
            if arr[num] < arr[marker]:
                arr[marker], arr[num] = arr[num], arr[marker]

        marker += 1
    return arr

# TEST
l =[6,8,1,4,10,7,8,9,3,2,5]

print(selection_sort_ola(l))
assert selection_sort_ola(l) == [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10], "BUG: Sorting failed! Should return [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]"
#

def selection_sort(alist):
    spot_marker = 0
    while spot_marker < len(alist):
        for num in range(spot_marker, len(alist)):
            if alist[num] < alist[spot_marker]:
                alist[spot_marker], alist[num] = alist[num], alist[spot_marker]
        spot_marker += 1
    return alist



# TEST
# print(selection_sort(l))
# assert selection_sort(l) == [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10], "BUG: Sorting failed! Should return [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]"
