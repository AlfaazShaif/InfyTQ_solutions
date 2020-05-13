#PF-Exer-22

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    #Write your logic here
    for index in range(0,no_of_passengers):
        ticket_details = airline + ':' + source[0:3] + ':' + destination[0:3] + ':' + str(101+index)
        ticket_number_list.append(ticket_details)

    if len(ticket_number_list) > 5:
        return ticket_number_list[len(ticket_number_list)-5::]
    #Use the below return statement wherever applicable
    return ticket_number_list

#Provide different values for airline,source,destination,no_of_passengers and test your program
print(generate_ticket("AI","Bangalore","London",7))