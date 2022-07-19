nums = [-2,-1,-3,-4,-1,-2,-11,-7,-6]

def maxSubArray(nums) -> int:

    if not nums:
        return 0

    curSum = maxSum = nums[0]

    for num in nums[1:]:
        temp = curSum + num
        curSum = max(num, temp) #如果num單個比先前的所有數再加上num還大，那前面就是累贅，從num開始算(curSum = num)，不然就繼續加下去(curSum = curSum + num)
        maxSum = max(maxSum, curSum)
    return maxSum



print(maxSubArray(nums))

def otherMaxSubArray(nums):
    summ = nums[0]
    c_sum  = 0
    for i in nums :
        c_sum += i
        summ = c_sum if c_sum > summ else summ
        if c_sum < 0 :
            c_sum = 0
    return summ

print(otherMaxSubArray(nums))