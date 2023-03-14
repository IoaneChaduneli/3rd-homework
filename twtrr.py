text = input("Enter a Word: ")

text_1 = list(text)

for char in text:
    match char:
        case 'a' | 'e' | 'i' | 'o' | 'u':
            text_1.remove(char)
            short_text = "".join(text_1)

print(short_text)