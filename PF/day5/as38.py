#PF-Assgn-38

def check_double(number):
    double = number * 2
    number = sorted(list(str(number)))
    double = sorted(list(str(double)))
    num = int("".join(number))
    doub = int(''.join(double))
    if num - doub == 0:
        return True
    else:
        return False
    #Remove pass and write your logic here

#Provide different values for number and test your program
print(check_double(125874))