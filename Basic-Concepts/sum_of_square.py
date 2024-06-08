def sum_of_square(list_a):
    sum = 0 
    for num in list_a:
        sum += num*num 


    return sum



list_a = [1,2,3,4,5]

result = sum_of_square(list_a)
print(result)