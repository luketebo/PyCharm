with open("sort.text", "r", encoding="UTF-8") as f:
    text = f.read()

# print(text.split('\n'))
new_text = text.split('\n')

for item in new_text:
    count = 0
    for i in range(len(item)):
        if item[i] == '.':
            count += 1
    with open("new_sort.text", "a", encoding="UTF-8") as f:
        f.write((count * " ") + item + '\n')
