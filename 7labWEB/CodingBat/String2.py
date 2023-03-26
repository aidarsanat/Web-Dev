# String 2

# def double_char(str):
#   result = ""
#   for i in range(0,len(str)):
#     result+=str[i]+str[i]
#   return result


# def count_code(str):
#   x=["co"+i+"e" for i in str.lower()]
#   count = 0
#   index = 0
#   for i in x:
#       if i in str[index:]:
#           index = str.find(i)+1
#           count+=1
#   return count


# def count_hi(str):
#   count = 0
#   for i in range(len(str)-1):
#       if str[i:i+2] == "hi":
#           count += 1

#   return count


# def end_other(a, b):
#   a = a.lower()
#   b = b.lower()

#   return a.endswith(b) or b.endswith(a)


# def cat_dog(str):
#   cat = 0
#   dog = 0

#   for i in range(len(str) - 2):
#       if str[i:i+3] == "cat":
#           cat += 1
#       elif str[i:i+3] == "dog":
#           dog += 1

#   return cat == dog


def xyz_there(str):
  if str[:3] == "xyz":
      return True
  for i in range(1, len(str) - 2):
      if str[i-1] != "." and str[i:i+3] == "xyz":
          return True
  return False
