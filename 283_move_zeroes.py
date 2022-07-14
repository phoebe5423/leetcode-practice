nums = [4, 0, 1, 0, 3, 12]
def moveZeroes(self, nums: List[int]) -> None:
    noneZeroCount=0     # count how many none zero number
    for i in range(len(nums)):
        if nums[i] !=0:
            if noneZeroCount != i:
                nums[noneZeroCount], nums[i]=nums[i],num[noneZeroCount]     # 第幾個非0數字就換到第幾位
            noneZeroCount=noneZeroCount+1