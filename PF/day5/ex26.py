#PF-Exer-26

def factorial(number):
    # pass #remove pass and write your logic to find and return the factorial of given number
    if number == 0:
        return 1
    return number * factorial(number - 1)


def find_strong_numbers(num_list):
    # pass #remove pass and write your logic to find and return the list of strong numbers from the given list
    temp_list = []
    for number in num_list:
        temp_sum = 0
        temp_number = number
        while temp_number>0:
            temp_sum += factorial(temp_number % 10)
            temp_number = temp_number // 10
        if number == temp_sum:
            temp_list.append(number)
    return temp_list
    

# num_list=[145,375,100,2,10]
num_list=[145, 375, 100, 2, 10, 40585, 0]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)

# print( factorial(5))