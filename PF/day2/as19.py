#PF-Assgn-19

def calculate_bill_amount(food_type,quantity_ordered,distance_in_kms):
    if quantity_ordered > 0 and distance_in_kms > 0:
        bill_amount=0
        if food_type == "V":
            food_cost = quantity_ordered * 120
        elif food_type == "N":
            food_cost = quantity_ordered * 150
        else:
            return -1
        cost_per_km = [(0,3),(3,6),(6,7)]
        delivery_cost = 0
        covered_distance = 0
        while covered_distance <= distance_in_kms:
            for distance in cost_per_km:
                if covered_distance <= distance[1]:
                    temp_delivery_cost = distance[0]
                    break
            delivery_cost += temp_delivery_cost
            covered_distance += 1
        
        bill_amount = food_cost + delivery_cost
        return bill_amount
    else:
        return -1

#Provide different values for food_type,quantity_ordered,distance_in_kms and test your program
bill_amount=calculate_bill_amount("N",2,7)
print(bill_amount)