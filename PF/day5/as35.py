#PF-Assgn-35

#Global variable
list_of_marks=(12,18,25,24,2,5,18,20,20,21)

def find_more_than_average():
    #Remove pass and write your logic here
    average = 0
    sum = 0
    count = 0
    for num in list_of_marks:
        sum += num
    average = sum / len(list_of_marks)
    for num in list_of_marks:
        if num > average:
            count+=1
    percent = (count/len(list_of_marks)) * 100
    return percent

def sort_marks():
    #Remove pass and write your logic here
    temp_list = []
    for num in list_of_marks:
        temp_list.append(num)
    return sorted(temp_list)

def generate_frequency():
    #Remove pass and write your logic here
    temp_list = [0]*26
    for num in list_of_marks:
        temp_list[num] += 1
    return temp_list

print(find_more_than_average())
print(generate_frequency())
print(sort_marks())