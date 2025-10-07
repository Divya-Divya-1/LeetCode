from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4]  # You can modify this
    sol = Solution()
    result = sol.productExceptSelf(nums)
    print(f"Input: {nums}")
    print(f"Output: {result}")
