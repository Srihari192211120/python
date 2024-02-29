def count_special_characters(statement):
    special_characters = 0
    for char in statement:
        if not char.isalnum() and char != ' ':
            special_characters += 1
    return special_characters

statement = "Modi Birthday @ September 17, #&$% is the wishes code for him."
special_count = count_special_characters(statement)
print("Number of special Characters:", special_count)

