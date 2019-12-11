def line_search(alist, key):
    for item in alist:
        if item == key:
            return True
    return False


key = 15
alist = [10,20,30,40,50,60]
print("Item {} found in {}? ".format(key, alist), line_search(alist, key))