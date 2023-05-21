def search(nums: list[int], target: int) -> int:
    def bfs(L, R):
        if R >= L:
            pivot = (R + L) // 2
            if target == nums[pivot]:
                return pivot
            elif target < nums[pivot]:
                return bfs(L, R - 1)
            else:
                return bfs(pivot + 1, R)
        else:
            return -1

    return bfs(0, len(nums) - 1)

"""
Drivers 
"""

nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(search(nums, target))
