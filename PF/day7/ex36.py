def create_largest_number(number_list):
    rev_number_list = number_list.sort(reverse = True)
    sum = ""
    for i in rev_number_list:
        sum += str(i)
    
    sum = int(sum)
    return sum
    #remove pass and write your logic here
    
number_list=[23,45,67]
largest_number = create_largest_number(number_list)
print(largest_number)