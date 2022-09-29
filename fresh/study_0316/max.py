a = float(input("奖金"))
reward = 0
if a >= 100:
    reward = (a-100) * 0.01 + (a-100-60) * 0.015 + ()
elif 60 <= a < 100:
    reward = (a - 60) * 0.0
elif 40 <= a < 60:
    reward = 10 * 1
elif 20 <= a < 40:
    reward = 1 * 0.1 + 1*0.75 + (a -2)*0.05
elif 10 <= a < 20:
    reward = 1 * 0.1 + (a - 1) * 0.75
else:
    reward = a * 0.1
print("奖金：" + str(reward))
