weight = float(input("input:"))
height = float(input("input:"))

bmi = weight / (height * height)

if bmi < 18.5:
    print("瘦")
elif 18.5 <= bmi <= 24:
    print("normal")
elif 24 < bmi <= 28:
    print("胖")
elif bmi >= 28:
    print("肥")
