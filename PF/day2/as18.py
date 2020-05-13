# #PF-Tryout

# def convert_currency(amount_needed_inr,current_currency_name):
#     current_currency_amount=0
#     #write your logic here
#     if(current_currency_name == "Euro"):
#         current_currency_amount = amount_needed_inr * 0.01417
#     elif(current_currency_name == "British Pound"):
#         current_currency_amount = amount_needed_inr * 0.0100
#     elif(current_currency_name == "Australian Dollar"):
#         current_currency_amount = amount_needed_inr * 0.02140
#     elif(current_currency_name == "Canadian Dollar"):
#         current_currency_amount = amount_needed_inr * 0.02027
#     else:
#         current_currency_amount = -1

#     return round(current_currency_amount,2)
    
#     #Euro	0.01417 #British Pound	0.0100  #Australian Dollar	0.02140
#     #Canadian Dollar	0.02027

# #Provide different values for amount_needed_inr,current_currency_name and test your program
# currency_needed=convert_currency(4500,"Canadian Dollar")
# if(currency_needed!= -1):
#     print(currency_needed )
# else:
#     print("Invalid currency name")



def convert_currency(amount_needed_inr,current_currency_name):
    exchange_rate = {
        'Euro': 0.01417,
        'British Pound': 0.0100,
        'Australian Dollar': 0.02140,
        'Canadian Dollar':0.02027
    }
    print(exchange_rate.items())
    for currency,equivalent_rate in exchange_rate.items():
        if currency == current_currency_name:
            current_currency_amount = amount_needed_inr * equivalent_rate
            return current_currency_amount
    
    return -1

currency_needed=convert_currency(2000,"Euro")
currency_needed=convert_currency(3500,"British Pound")
if(currency_needed!= -1):
    print(currency_needed )
else:
    print("Invalid currency name")