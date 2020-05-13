def binarySearch(list, low, high, element):
    while low <= high:
        mid = (low + high - 1)//2
        if list[mid] == element:
            return mid
        elif list[mid] < element:
            low = mid + 1
        else:
            hight = mid - 1

    return -1

list = [4, 2, 6 ,7, 8, 9]
result = binarySearch(list, 0, len(list), 9)

if result != -1:
    print("found at " +str(result))
else: 
    print("not found")