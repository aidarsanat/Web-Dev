# List 2

# def count_evens(nums):
#   cnt = 0
#   for i in nums:
#     if i%2 == 0:
#       cnt += 1
#   return cnt


# def sum13(nums):
#     sm = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] == 13:
#             i += 1
#         else:
#             sm += nums[i]

#         i += 1

#     return sm


# def big_diff(nums):
#     mn = nums[0]
#     mx = nums[0]

#     for i in range(1,len(nums)):
#         mn = min(mn, nums[i])
#         mx = max(mx, nums[i])

#     return mx- mn


# def sum67(nums):
#     res = 0
#     a = False

#     for i in range(len(nums)):
#         if nums[i] == 6:
#             a = True
#         if not a:
#             res += nums[i]
#         if nums[i] == 7 and a:
#             a = False

#     return res


# def centered_average(nums):
#    return (sum(nums) - max(nums) - min(nums)) / (len(nums) - 2)


def has22(nums):
  for i in range(len(nums)-1):
    if nums[i] == 2 and nums[i+1] == 2:
      return True
  return False
