#PF-Assgn-22
def find_leap_years(given_year):

    # Write your logic here
    temp_year = given_year
    leap_year_list = []
    while(len(leap_year_list) < 16):
        if(temp_year%4 == 0 and temp_year%100 != 0) or (temp_year%400 == 0):
            leap_year_list.append(temp_year)
        temp_year += 1
    print(len(leap_year_list))
    return leap_year_list

list_of_leap_years=find_leap_years(2000)
print(list_of_leap_years)