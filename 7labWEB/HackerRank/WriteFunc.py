def is_leap(a):
    leap = False
    if (a % 4 == 0 and a%100 != 0) or (a%400 == 0):
        leap = True
    else:
        leap = False

    return leap

year = int(input())
print(is_leap(year))