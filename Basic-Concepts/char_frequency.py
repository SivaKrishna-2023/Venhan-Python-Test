def char_frequency(text):
    char_count = {}

    for char in text:
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1 

    return char_count


text = "Hello, world! This is a test string."
result = char_frequency(text)
print(result)