class Solution:
    """
        Pretty simple caching solution
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Cache stores two types of values: possible numbers and previous valid combinations
        cache = set()
        output = []
        while len(nums) > 0:
            # The current number we use is popped here because it will
            # be stored in the cache and we won't need to reference it outside the cache
            num = nums.pop()
            # Loop through what's left of the array
            for num1 in nums:
                # Find the number we need to reach 0
                inverse = -(num + num1)
                # Let's us check the cache for duplicate solutions. It's sorted so order
                # won't change the hash, a string because a list can't be hashed
                combString = str(sorted([inverse, num, num1]))
                # Checks for a valid, unique combination
                if inverse in cache and combString not in cache:
                    output.append([inverse, num, num1])
                    cache.add(combString)
            # Current number is added here so we don't accidentally grab duplicates
            if num not in cache:
                cache.add(num)
        return output