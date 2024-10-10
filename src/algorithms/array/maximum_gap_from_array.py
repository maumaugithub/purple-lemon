from typing import List


class MaximumGap:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def calculate_maximum_gap(self) -> int:
        n = len(self.nums)
        max_gap = 0
        if n > 1:
            sorted_nums: List[int] = self.nums
            sorted_nums.sort()
            for i in range(n-1):
                local_gap = sorted_nums[i+1] - sorted_nums[i]
                if local_gap > max_gap:
                    max_gap = local_gap
        return 0 if n <= 1 else max_gap
