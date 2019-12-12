def bisection_iter(n, arr):
    '''Iterative approach to Bisection search'''
    start = 0
    stop = len(arr) -1
    while start <= stop:
        mid = (start + stop)//2
        print(arr[mid])

        if n == arr[mid]:
            return f"{n} found at at index {mid}"
        elif n > arr[mid]:
            start = mid + 1
        else:
            stop = mid - 1

    return f"{n} not found in list"


def create_list(max_val):
    arr = []
    for num in range(1, max_val + 1):
        arr.append(num)
    return arr


# TEST
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
l = create_list(11)
print(l)
for num in range(17):
    print(bisection_iter(num,l))
