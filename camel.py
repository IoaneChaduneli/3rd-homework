text = input("Enter CamelCase: ")
text_2 = list(text)


for char in text:
    if char.isupper():
        index = text_2.index(char)
        if index > 0:
            text_2.insert(text_2.index(char),"_")
            new_text = "".join(text_2)

print("snake_case:",new_text)
       





