"""
输入：nums = [2,7,11,15], target = 9
输出：[0,1]
"""


class Solution:
    def two_Sum(self, nums: list[int], target: int) -> list[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            if hashmap.get(target - value) is not None:
                return [index, hashmap.get(target - value)]
            hashmap[value] = index


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    result = s.two_Sum(nums, target)
    print(result)


