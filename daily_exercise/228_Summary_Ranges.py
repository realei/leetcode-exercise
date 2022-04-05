class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        res = []
        stack = []
        for i in range(len(nums)):
            if not stack:
                stack.append(nums[i])
            elif nums[i] - stack[-1] == 1:
                stack.append(nums[i])
            else:
                if len(stack) == 1:
                    res.append(str(stack.pop()))
                    stack.append(nums[i])
                else:
                    res.append("->".join([str(stack.pop(0)), str(stack.pop())]))
                    stack = []
                    stack.append(nums[i])

        if len(stack) == 1:
            res.append(str(stack.pop()))
            stack.append(nums[i])
        else:
            res.append("->".join([str(stack.pop(0)), str(stack.pop())]))
            stack = []
            stack.append(nums[i])

        return res
