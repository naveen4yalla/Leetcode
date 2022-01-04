class Solution:
    def removeDuplicates(self, nums):
        count=0
        for f in range(len(nums)):
            if nums[count]!=nums[f]:
                count+=1
                nums[count]=nums[f]
        return count+1
s=Solution()
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))