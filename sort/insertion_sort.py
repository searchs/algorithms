def insertion_sort(alist):
    # O(n2)
    marker = 1
    while marker < len(alist):
        for num in range(len(alist)):
            if alist[marker] < alist[num]:
                alist[num], alist[marker] = alist[marker], alist[num]

        marker += 1
    return alist


l = [6,1,8,4,10]
print(insertion_sort(l))
assert insertion_sort(l) == [1,4,6,8,10], "BUG:  Issues with Insertion Sort!"
e = [1]
assert insertion_sort(e) == [1], "BUG:  Issues with Insertion Sort!"


lg = [3,4,5,2,3,1,7,1,8,9,1,2,4,6,7,9,8]
assert insertion_sort(lg) == [1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 8, 8, 9, 9], "BUG:  Issues with Insertion Sort!"
