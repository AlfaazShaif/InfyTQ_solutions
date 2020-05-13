#PF-Assgn-30

def encode(message):
    pass
    #Remove pass and write your logic here
    message += "0"
    msg = ''
    count = 1
    for index, value in enumerate(message):
        if index < len(message)-1:
            if value == message[index+1]:
                count += 1
            else:
                msg += str(count) + value
                count=1
    return msg

#Provide different values for message and test your program
encoded_message=encode("ABBBBCCCCCCCCAB")
print(encoded_message)