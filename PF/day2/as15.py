def find_product(num1, num2, num3):
    arguments = [num1, num2, num3]
    product = 1

    if 7 in arguments:
        i = arguments.index(7)
        if i == (len(arguments) - 1):
            return -1
    else:
        i = -1

    for index in range(i+1, len(arguments)):
        product *= arguments[index]
        
    return product


product = find_product(7,6,2)
print(product)