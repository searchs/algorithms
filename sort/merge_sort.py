def merge_sort(arr1, arr2):
    sorted_arr = []
    i,j = 0,0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1

    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1

    return sorted_arr


# TEST
l1 = [1, 4, 6, 8, 10]
l2 = [2, 3, 5, 7, 8, 9]

# print(f"Merged List: {merge_sort(l1,l2)}")

def divide_arr(arr):
    if len(arr) < 2:
        return arr[:]
    else:
        middle = len(arr)//2
        l1 = divide_arr(arr[:middle])
        l2 = divide_arr(arr[middle:])
        return merge_sort(l1,l2)


# l = [4,1]
l =[6,8,1,4,10,7,8,9,3,2,5]
print(divide_arr(l))
