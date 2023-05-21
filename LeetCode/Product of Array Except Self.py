def productExceptSelf(nums: list[int]) -> list[int]:
    answer = [1] * len(nums)

    preNum = 1
    for i in range(len(nums)):
        answer[i] = preNum
        preNum *= nums[i]

    postNum = 1
    for i in range(len(nums) - 1, -1, -1):
        answer[i] *= postNum
        postNum *= nums[i]
    return answer


nums = [3, 4, 2, 3]
print(productExceptSelf(nums))


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))