class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)

    def add(self, val: int) -> int:
        flag = 0
        for i,x in enumerate(self.nums):
            if val >= x:
                self.nums.insert(i, val)
                flag = 1
                break
        if not flag:
            self.nums.append(val)
        return self.nums[self.k-1]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)