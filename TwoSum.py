def TwoSum(nums,target):
    dict={}
    for i in range(len(nums)):
        if nums[i] in dict:
            return [dict[nums[i]] ,i]
        else:
            dict[target-nums[i]]=i



print(TwoSum([1,3,4,5,7],12))