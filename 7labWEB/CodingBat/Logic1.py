# Logic 1

# def cigar_party(cigars, is_weekend):
#   if is_weekend == False and (cigars < 40 or cigars > 60):
#     return False
#   elif is_weekend == True and cigars < 40:
#     return False
#   else:
#     return True


# def caught_speeding(speed, is_birthday):
#   if is_birthday == False:
#     if speed <= 60:
#       return 0
#     elif speed >= 61 and speed <= 80:
#       return 1
#     else:
#       return 2
#   else:
#     if speed <= 65:
#       return 0
#     elif speed >= 66 and speed <= 85:
#       return 1
#     else:
#       return 2


# def love6(a, b):
#   if a == 6 or b == 6 or a+b == 6 or abs(a-b) == 6:
#     return True
#   else:
#     return False


# def date_fashion(you, date):
#   if you <= 2 or date <= 2:
#     return 0
#   elif you >= 8 or date >= 8:
#     return 2
#   else:
#     return 1


# def sorta_sum(a, b):
#   if a+b >=10 and a+b <=19:
#     return 20
#   else:
#     return a+b


# def in1to10(n, outside_mode):
#   if n >=1 and n <=10 and outside_mode == False:
#     return True
#   if outside_mode == True and (n <= 1 or n >=10):
#     return True
#   else:
#     return False


# def squirrel_play(temp, is_summer):
#   if temp >= 60 and temp <=90 and is_summer == False:
#     return True
#   elif is_summer ==True and temp >= 60 and temp <=100:
#     return True
#   else:
#     return False


# def alarm_clock(day, vacation):
#   if vacation == True and (day == 6 or day == 0):
#     return "off"
#   elif vacation == True and day != 6 and day != 0:
#     return "10:00"
#   elif vacation == False and (day == 6 or day == 0):
#     return "10:00"
#   else:
#     return "7:00"


def near_ten(num):
  return (num + 2) % 10 <= 4
