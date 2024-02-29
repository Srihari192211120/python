input_str = "this is a cat"
words = input_str.split()
result = ".".join(word[0].upper() for word in words)
print(result)
