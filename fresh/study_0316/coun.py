year = int(input())

## 1959 1931 year%4==0 and year%100!=0 or year%400==0:


if year <= 0:
    print("what are you doing?")
else:
    if year == 1959:
        print("建国十年")
    elif year == 1931:
        print("建党十年")
    elif year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print("闰年")
