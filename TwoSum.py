from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]
            if total == target:
                return [left + 1, right + 1]  # 1-indexed
            elif total < target:
                left += 1
            else:
                right -= 1
        return []


if __name__ == "__main__":
    # You can modify these values or take input interactively
    numbers = [2, 7, 11, 15]
    target = 9

    sol = Solution()
    result = sol.twoSum(numbers, target)
    print(f"Input: numbers = {numbers}, target = {target}")
    print(f"Output: {result}")

