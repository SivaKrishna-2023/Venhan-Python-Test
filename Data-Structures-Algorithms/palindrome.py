def is_palindrome(s): 
    normalized_str = ''.join(filter(str.isalnum, s)).lower()
    

    return normalized_str == normalized_str[::-1]


print(is_palindrome("A man, a plan, a canal, Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))  # False