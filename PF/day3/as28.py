# #PF-Assgn-28

def sum_of_digit(num):
    sum = 0
    while(num > 0):
        sum += num%10
        num = num//10
    return sum

def find_max(num1, num2):
    max_num=-1
    # Write your logic here
    num_list = []
    if num1 < num2:
        for i in range(num1,num2+1):
            if sum_of_digit(i) % 3 == 0 and i % 5 == 0:
                if i < 100:
                    num_list.append(i)
        if num_list != []: 
        # if num_list: 
            max_num = max(num_list)   
    return max_num

# Provide different values for num1 and num2 and test your program.
max_num=find_max(10,15)
print(max_num)

# num = 23
# print(len(str(num)))
# num = 100
# print(len(str(num)))
