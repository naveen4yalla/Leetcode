# #Brute force approach Time complexity O(n²) Space Complexity O(1)
# def two_sum(nums,target):
#     for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 if nums[j] == target - nums[i]:
#                     return [i, j]







#Hashmap approach Time complexity O(n) Space Complexity O(n)
def two_sum(nums,target):
    hashmap={}
    for i,j in enumerate(nums):
        temp=target-j
        if temp in hashmap:
            return i,hashmap[temp]
        else:
            hashmap[j] = i
