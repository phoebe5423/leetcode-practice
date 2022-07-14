#store in dictionary 
def containsDuplicate(self, nums: List[int]) -> bool:
    freq = dict()
    for i in range(len(nums)):
        if nums[i] not in freq: 
            freq[nums[i]] = 1
        else:
            return True
    return False

#store in list
def containsDuplicate(self, nums: List[int]) -> bool:
    duplicate = []
    for i in nums:
        if i in duplicate:
            return True
        else:
            duplicate.append(i)
    return False

# convert to set. Because set doesn't allow duplicated values, the lenth will be different if duplicated values exist
def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)