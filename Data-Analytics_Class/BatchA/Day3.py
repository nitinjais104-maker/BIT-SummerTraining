arr = [1,[2,3],[4,[5,6]], 7]


def flatten_array(arr):
    stack = arr[::-1]
    result = []
    while len(stack) > 0:
        item = stack.pop()
        if type(item) == list:
            for value in item[::-1]:
                stack.append(value)
        else:
            result.append(item)
    return result 



# Output -> [1,2,3,4,5,6,7]


# Step    Stack Before         items = stack .pop()       Action      Result      Stack After
# 1       [7,[4,[5,6]],[2,3],1].  1                       Not List, result [1]          [7,[4,[5,6]],[2,3]]  
# 2          [7,[4,[5,6]],[2,3]]  [2,3]                      3,2         [1]          [7,[4,[5,6]],3,2]
# 3       [7,[4,[5,6]],3,2]       2                       Not list        [1,2]       [7,[4,[5,6]],3]


# name marks
# 2. Rahul   80
# 1. Aman    99