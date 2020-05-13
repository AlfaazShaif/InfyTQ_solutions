#PF-Assgn-33

def find_common_characters(msg1,msg2):
    # pass #Remove pass and write your logic here
    if msg1 is msg2:
        return msg1
    else:
        msg1 = msg1.replace(" ", '')
        msg2 = msg2.replace(" ", '')
        msg = ''
        for letter in msg1:
            if letter in msg2:
                msg += letter
        if msg != '':
            return msg
        else:
            return -1

#Provide different values for msg1,msg2 and test your program
msg1="I like Python"
msg2="Java is a very popular language"
# msg1 = 'moto'
# msg2 = 'moto'
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
