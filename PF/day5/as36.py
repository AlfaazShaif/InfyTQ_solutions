#PF-Assgn-36
def create_largest_number(number_list):
    #remove pass and write your logic here
    number_list.sort(reverse=True)
    temp_num = ''
    for num in number_list:
        temp_num += str(num)
    return int(temp_num)

number_list=[23,45,67]
largest_number=create_largest_number(number_list)
print(largest_number)