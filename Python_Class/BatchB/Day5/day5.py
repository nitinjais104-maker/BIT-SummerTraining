# Reverse a list 

# nums = [10, 20, 30, 40, 50]

# left = 0
# right = len(nums) - 1

# while left < right:
#     nums[left], nums[right] = nums[right], nums[left]
#     left += 1
#     right = right -1

# print(nums)

#output -> [50,40,30,20,10]

# Stack 

# stack = []

# stack.append(10)
# stack.append(20)
# print(stack)

# top = stack.pop()
# print(top)
# print(stack)

# stack = []

# stack.pop()
# if stack:
#     stack.pop()

# Queue

# queue = []

# queue.append("A")
# queue.append("B")
# queue.append("C")
# print(queue)

# first = queue.pop(0)

# print(first)


# from collections import deque

# queue = deque()

# queue.append("A")
# queue.append("B")
# queue.append("C")

# print(queue)

# print(queue.popleft())

#heapq

# import heapq
# nums = [5,2,8,1,3]

# heapq.heapify(nums)

# print(nums)

# print(heapq.heappop(nums))

# import heapq
# heap = []

# heapq.heappush(heap, 30)
# heapq.heappush(heap, 10)
# heapq.heappush(heap, 20)
# heapq.heappush(heap, 5)

# print("Heap:", heap)

# print("Samllest:", heap[0])
# print("Removed:", heapq.heappop(heap))
# print("After remove:", heap)

import heapq 

nums = [5,1,9,3,7,2]

top_3 = heapq.nlargest(3, nums)
smallest_toip_3 = heapq.nsmallest(3, nums)

print(top_3)
print(smallest_toip_3)