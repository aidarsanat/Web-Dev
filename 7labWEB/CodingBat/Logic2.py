# Logic 2

# def make_bricks(small, big, goal):
#   return (goal%5)<=small and (goal-(big*5))<=small


# def fix_teen(n):
#     if (n >= 13 and n <=19):
#         if (n!= 15 and n != 16):
#             n = 0
#     return n
# def no_teen_sum(a, b, c):
#   return fix_teen(a)+fix_teen(b)+fix_teen(c)


# def make_chocolate(small, big, goal):
#   if small + big * 5 < goal or small < goal%5 :
#     return -1
#   elif((big * 5) > goal):
#     return goal % 5
#   else:
#     return goal - big * 5


# def lone_sum(a, b, c):

#   if a != b and b != c and c != a:
#     return a + b + c

#   elif a == b == c:
#     return 0

#   elif a == b:
#     return c
#   elif b == c:
#     return a
#   elif c == a:
#     return b


# def round_sum(a, b, c):
#   def round10(n):
#     return (n+5)/10*10

#   return round10(a) + round10(b) + round10(c)


# def lucky_sum(a, b, c):
#   if a==13:
#     return 0
#   elif b==13:
#     return a
#   elif c==13:
#     return a+b
#   else:
#     return a+b+c


def close_far(a, b, c):
  return (abs(a - b) <= 1 or abs(a - c) <= 1) and abs(c - a) >= 2 <= abs(c - b) or abs(b - a) >= 2 <= abs(b - c)
