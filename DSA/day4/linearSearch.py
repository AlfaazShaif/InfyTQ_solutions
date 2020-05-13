def linearSearch(list, element):
    index = 0
    while index < len(list):
        if element == list[index]:
            return index
        index += 1
    return -1

list = [4, 2, 6 ,7, 8, 9]
result = linearSearch(list, 7)
if result != -1:
    print("Found at: "+str(result + 1))
else:
    print("Not found")