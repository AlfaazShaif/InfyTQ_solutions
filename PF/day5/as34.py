#PF-Assgn-34
def find_pairs_of_numbers(num_list,n):
    # pass
    #Remove pass and write your logic here
    count = 0
    temp_list = []
    for number in num_list:
        if (n - number) in num_list[num_list.index(number)+1:]:
            count += 1
            # temp_list.append(number)
            # temp_list.append(n - number)
    # return temp_list
    return count

num_list=[-1, 1, 2, 7, 4, 5, 6, 0, 3]
n=6
print(find_pairs_of_numbers(num_list,n))