import random


def judge(a, op, b) -> int:
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "/":
        return a / b
    elif op == "*":
        return a * b
    else:
        print("操作符出错")
        return 0


count = 0
op_t = '+-*/'
while count < 20:
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    op = random.choice(op_t)
    text_n = str(a) + op + str(b) + "=" + "\n"
    with open("no_answer.text", "a") as w:
        w.write(text_n)
    text_t = str(a) + op + str(b) + "=" + '{:.2f}'.format(judge(a, op, b)) + "\n"
    with open("answer.text", "a") as nw:
        nw.write(text_t)
    count += 1

