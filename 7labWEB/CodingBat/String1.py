# String1
# def hello_name(name):
#   result = "Hello " + name + "!"
#   return result

# def make_out_word(out, word):
#     result = out[:2] + word + out[2:]
#     return result


# def first_half(str):
#   result = str[:len(str)/2]
#   return result


# def non_start(a, b):
#   result = a[1:] + b[1:]
#   return resultv


# def make_abba(a, b):
#   result = a+b+b+a
#   return result


# def extra_end(str):
#   result = str[-2:] + str[-2:] + str[-2:]
#   return result


# def without_end(str):
#   result = str[1:-1]
#   return result


# def left2(str):
#   result = str[2:] + str[:2]
#   return result


# def make_tags(tag, word):
#   result = "<" + tag + ">" + word + "</" + tag + ">"
#   return result


# def first_two(str):
#   result = str[:2]
#   return result


def combo_string(a, b):
  if len(a) < len(b):
    result = a+b+a
  else:
    result = b+a+b
  return result
