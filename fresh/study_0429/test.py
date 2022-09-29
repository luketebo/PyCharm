import json

with open("identify.text", "r") as f:
    content = f.read()

context_dict = json.loads(content)

print(context_dict)

input_num = input("请输入区域号")

if input_num in context_dict.keys():
    print(context_dict[input_num])
else:
    print("没有该地址")
