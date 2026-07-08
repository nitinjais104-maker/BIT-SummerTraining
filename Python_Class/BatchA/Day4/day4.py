# Reverse a list

# nums = [10, 20, 30, 40, 50]
# print(nums[::-1])

# [start:end:step]
# left = 0
# right = len(nums) - 1


# while left < right: 
#     nums[left], nums[right] = nums[right], nums[left]

#     left += 1
#     right -= 1
# print(nums)

#output : [50, 40, 30, 20, 10]


# Find Largest number

# nums = [10, 50, 20, 100,5] #output = 100
# largest = nums[0]

# for num in nums:
#     if num > largest:
#         largest = num

# print(largest)


# 3. Find second largest number

# nums = [10, 20, 30, 40,50] # Output -> 40

# largest = float("-inf")
# second_largest = float("-inf")

# for num in nums:
#     if num > largest:
#         second_largest = largest
#         largest = num
#     elif num > second_largest and num != largest:
#         second_largest = num
# print(second_largest)


# Step        num      condtion    largest    second_largest
# Start       -           -           -inf    -inf
# 1           10          10 > largest 10         -inf
# 2           20        20 > largest     20       10
# 3           30          30 > largest    30  20
# 4           40          40> largest     40   30
# 5           50          50 > largest        50      40

# nums = [50, 10, 40, 20, 30]

# Step    Num      What Happen    largest     second_largest
# 1       50         New largest found    50      -inf
# 2       10                      50          10
# 3       40                      50          40

#4. Find Duplicate 
# nums = [1,2,3,4,2] #-> Duplicate Found

# seen = set()

# for num in nums:
#     if num in seen:
#         print("Duplicate Found")
#         break
#     seen.add(num)


# 5. Frequency Count

# text = "banana"

# freq = {}

# for ch in text:
#     if ch in freq:
#         freq[ch] += 1
#     else:
#         freq[ch] = 1
# print(freq)

# for key, value in freq.items():
#     print(f"{key}:{value}")

#output
# b: 1
#a : 3
# n : 2

#6. isAnagram

# s = "listen"
# t = "silent"
# # print(sorted(s) == sorted(t))
# freq = {}
# for ch in s:
#     freq[ch] = freq.get(ch,0) + 1

# for ch in t:
#     freq[ch] = freq.get(ch, 0) - 1

# for val in  freq.values():
#     if val != 0:
#         print(False)
#         break
# else:
#     print(True)

#7. Two Sum

nums = [2,7,11,15]
target = 9 
#output : [0,1]

# seen = {}

# for i, num in enumerate(nums):
#     diff = target - num
    #  needed = target - num 
    # target =9, num = 2
    # needed = 9 - 2 
    # needed = 7
    # if diff in seen:
    #     print([seen[diff], i])
    
    # seen[num] = i

left = 0
right = len(nums) - 1

while left < right:
    current_sum = nums[left] + nums[right]

    if current_sum == target:
        print([left, right])
        break
    elif current_sum > target:
        right -= 1
    else:
        left += 1