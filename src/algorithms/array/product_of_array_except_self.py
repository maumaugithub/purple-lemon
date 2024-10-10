from typing import List


# Problem:
# "Given an array nums of n integers where n > 1,
# return an array output such that output[i] is equal to the product of all the elements of nums
# except nums[i]."
# Assumptions:
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
class ArrayProduct:
    def __init__(self, nums: List[int]):
        self.nums = nums

    def product_except_self(self) -> List[int]:
        n = len(self.nums)
        prefix = [1] * n
        suffix = [1] * n

        for i in range(1, n):
            prefix[i] = prefix[i - 1] * self.nums[i - 1]

        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] * self.nums[i + 1]

        result = [prefix[i] * suffix[i] for i in range(n)]
        return result

    def product_except_self_o1(self) -> List[int]:
        n = len(self.nums)
        a = [1] * n
        
        for i in range(n - 2, -1, -1):
            a[i] = self.nums[i+1] * a[i+1]
            
        b = 1
        for j in range(1, n):
            b *= self.nums[j-1]
            a[j] *= b
        return a

    def product_except_self_poc(self) -> List[int]:
        prefix = suffix = 1
        n = len(self.nums)
        result = [1] * n

        for i in range(n):
            if i > 0:
                prefix = prefix * self.nums[i - 1]
            result[i] = prefix

        for i in range(n - 1, -1, -1):
            result[i] = result[i] * suffix
            suffix = suffix * self.nums[i]

        return result
