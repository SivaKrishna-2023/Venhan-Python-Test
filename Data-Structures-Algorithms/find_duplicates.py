def find_duplicates(arr):
    count_dict = {}
    
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    
    duplicates = []
    
    
    for num, count in count_dict.items():
        if count > 1:
            duplicates.append(num)
    
    return duplicates



arr = [1, 2, 3, 2, 4, 5, 1]
print(find_duplicates(arr))  # Output: [1, 2]
