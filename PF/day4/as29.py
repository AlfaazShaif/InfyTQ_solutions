#PF-Assgn-29
def calculate(distance,no_of_passengers):
    #Remove pass and write your logic here
    fuel_price = 70
    mileage_of_bus = 10
    ticket_price = 80
    if (distance * fuel_price)/mileage_of_bus > ticket_price * no_of_passengers:
        return -1
    else:
        return ticket_price * no_of_passengers - (distance * fuel_price)/mileage_of_bus



#Provide different values for distance, no_of_passenger and test your program
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))