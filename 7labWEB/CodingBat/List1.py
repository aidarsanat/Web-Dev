# List 1

# def first_last6(nums):
#   if nums[0] == 6 or nums[len(nums)-1] == 6:
#     return True
#   else:
#     return False


# def common_end(a, b):
#   if a[0] == b[0] or a[len(a)-1] == b[len(b)-1]:
#     return True
#   else:
#     return False

# def reverse3(nums):
#   result = []
#   for i in range(0,len(nums)):
#     result.append(nums[len(nums)-1-i])
#   return result


# def middle_way(a, b):
#   result = []
#   result.append(a[1])
#   result.append(b[1])
#   return result


# def same_first_last(nums):
#   if len(nums) >= 1 and nums[0] == nums[len(nums)-1]:
#     return True
#   else:
#     return False


# def sum3(nums):
#   return nums[0]+nums[1] + nums[2]


# def max_end3(nums):
#   result = []
#   mx = nums[len(nums)-1]
#   if nums[0] > nums[len(nums)-1]:
#     mx = nums[0]
#   for i in range(0,3):
#     result.append(mx)
#   return result


# def make_ends(nums):
#   result = []
#   result.append(nums[0])
#   result.append(nums[len(nums)-1])
#   return result

# def make_pi():
#   result = [3, 1, 4]
#   return result


# def rotate_left3(nums):
#   result = [nums[1], nums[2], nums[0]]
#   return result


# def sum2(nums):
#   if len(nums)>1:
#     return nums[0]+nums[1]
#   elif len(nums) == 1:
#     return nums[0]
#   else:
#     return 0


def has23(nums):
  if 2 in nums or 3 in nums:
    return True
  else:
    return False
