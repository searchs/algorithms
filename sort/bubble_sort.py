def bubble_sort(arr):
    # Always aim for O(nlogn)
    swap_occurred = True
    while swap_occurred:
        swap_occurred = False
        for num in range(len(arr) - 1):
            if arr[num] > arr[num + 1]:
                # print("Swapping....")
                swap_occurred = True
                arr[num],arr[num +1] = arr[num +1], arr[num]
                # print(arr)
        # else:
        #     print("No swap yet")
        #     print(arr)
        #     continue
            # holder = arr[num]
            # arr[num] = arr[num + 1]
            # arr[num + 1] = holder
        # bubble_sort(arr)
        # num = num + 1
    # print(arr)
    return arr

l =[6,8,1,4,10,7,8,9,3,2,5]
# print(bubble_sort(l))
bubble_sort(l)

# Performance Metrics
def perf_bubble_sort(arr):
    swap_occurred = True
    comparisons = 0
    while swap_occurred:
        comparisons += 1
        swap_occurred = False
        for num in range(len(arr) - 1):
            comparisons += 1
            if arr[num] > arr[num + 1]:
                print("Swapping....")
                swap_occurred = True
                arr[num],arr[num +1] = arr[num +1], arr[num]

    print("Comparisons: {}".format(comparisons))


'''pl =[6,8,1,4,10,7,8,9,3,2,5]

# perf_bubble_sort(pl)
# Best case
fl = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
perf_bubble_sort(fl)

ml = [6, 7, 8, 8, 9, 10,1, 2, 3, 4, 5]
perf_bubble_sort(ml)

# Worst Case
wl =  [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]
perf_bubble_sort(wl)'''


def perf_recur_bubble_sort(arr):
    swap_occurred = True
    comparisons = 0
    while swap_occurred:
        comparisons += 1
        swap_occurred = False
        for num in range(len(arr) - 1):
            comparisons += 1
            if arr[num] > arr[num + 1]:
                # print("Swapping....")
                swap_occurred = True
                arr[num],arr[num +1] = arr[num +1], arr[num]
        bubble_sort(arr)
        # num = num + 1
    print(comparisons)
    return arr


pl =[6,8,1,4,10,7,8,9,3,2,5]

perf_recur_bubble_sort(pl)
# Best case
fl = [1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10]
perf_recur_bubble_sort(fl)

ml = [6, 7, 8, 8, 9, 10,1, 2, 3, 4, 5]
perf_recur_bubble_sort(ml)

# Worst Case
wl =  [10, 9, 8, 8, 7, 6, 5, 4, 3, 2, 1]
perf_recur_bubble_sort(wl)