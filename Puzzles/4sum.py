class Solution:
    """
    Find all the potential pairs. Cache every pair and their indexes. The sum of the pair will be the key.
    As you go check if the current generated pair's value minus the target exists in the cache.
    Add valid combinations to output if they're not already present in combCache. Return output.
    """
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        valCache = {}
        combCache = set()
        output = []
        
        # We use a while loop so we can remove numbers from the input as we go. 
        # This prevents us from doing an aditional loop and checking that we aren't making a pair at the same index.
        # A similar setup could be done with ranges.
        i = len(nums) - 1
        while len(nums) > 0:
            num = nums.pop()
            
            for j, num1 in enumerate(nums):
                value = num + num1
                diff = target - value
                pair = [num, num1]
                
                if diff in valCache:
                    # It's possible to have several pairs that have the same sum. We check all possible pairs 
                    # to see if they don't share an index with the current pair.
                    for difPair in valCache[diff]:
                        
                        # difPair's indexes are stored in a set so we can do a quick check
                        if i not in difPair["indexes"] and j not in difPair["indexes"]:
                            comb = [num, num1] + difPair["pair"]
                            # We convert the combination to a sorted string so we have a consistent hashed value
                            # to check in our set.
                            sortComb = str(sorted(comb))
                            
                            if sortComb not in combCache:
                                combCache.add(sortComb)
                                output.append(comb)
                                
                if value not in valCache:
                    valCache[value] = [{"pair": pair, "indexes": {i,j}}]
                else:
                    valCache[value].append({"pair": pair, "indexes": {i,j}})
                
            i -= 1
        return output