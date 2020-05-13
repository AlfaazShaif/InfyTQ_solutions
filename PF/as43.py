def find_smallest_number(num):
    #start writing your code here
    count = 0
    i = 1
    while(i):
        j = 1
        while(j < num // 2):
            if(i%j == 0):
                count += 1
            j += 1
        if(count == num):
            result = count
            break
        
        i += 1
    
    #result = i
    return result
        
num=16
print("The number of divisors :",num)
result=find_smallest_number(num)
print("The smallest number having",num," divisors:",result)