#  数据加密 将每个字母用它后面5个字母代码

# ord()函数主要用来返回对应字符的ascii码，chr()主要用来表示ascii码对应的字符他的输入时数字
# 加密 v1.0
def password():
    n = input()
    new = []
    print(n)
    print("-----------")
    for i in range(len(n)):
        a = chr(ord(n[i]) + 5)
        new.append(a)

    print(new)


# 加密v2.0
num = input()
num_asc = ''
sum_num = 0
for i in range(6):
    # num_asc.append(ord(num[i]))
    num_asc += str(ord(num[i]))
    sum_num += ord(num[i])
# 把ascii进行拼接
unum_asc = num_asc[::-1]
unum_asc = int(unum_asc)
pwd = unum_asc + sum_num
print(pwd)

# 题目8：将考试座号A1-A30放入列表中，先输出一行“座位编码”，然后从下一行开始一次输出作为编号，使用两种方式进行列表输出


n = []
for i in range(1, 31):
    a = 'A' + str(i)
    n.append(a)
print(n)

print("座位编号")
print(n)
for i in range(30):
    print(n[i], end=' ')

print("\n")
for item in n:
    print(item, end=' ')
