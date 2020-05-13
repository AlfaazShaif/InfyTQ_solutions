#PF-Assgn-24
def form_triangle(num1,num2,num3):
    #Do not change the messages provided below
    success="Triangle can be formed"
    failure="Triangle can't be formed"
    
    tri_sides = [num1, num2, num3]
    for side in tri_sides:
        if side >= tri_sides[(tri_sides.index(side)+1) % 3] + tri_sides[(tri_sides.index(side)+2) % 3]:
            return failure
    return success

    #Write your logic here

    #Use the following messages to return the result wherever necessary
    # return success
    # return failure

#Provide different values for the variables, num1, num2, num3 and test your program
num1=3
num2=1
num3=5
result = form_triangle(num1, num2, num3)
print(result)