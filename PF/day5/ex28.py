#PF-Exer-28
                                              
#This method accepts the name of winner of each match of the day
def find_winner_of_the_day(*match_tuple):
    #Remove pass and write the logic here
    temp_list = list(match_tuple)
    temp_list.sort()
    if temp_list.count(temp_list[0]) > temp_list.count(temp_list[-1]):
        return temp_list[0]
    else:
        return temp_list[-1]

#Invoke the function with each of the print statements given below
print(find_winner_of_the_day("Team1","Team2","Team1"))
print(find_winner_of_the_day("Team1","Team2","Team1","Team2"))
