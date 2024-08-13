"""
Solution 1: Brute Force Method
This is the most straightforward approach, where you use two nested loops to check all possible pairs in the array to find the two numbers that add up to the target.

Time Complexity: 
𝑂(𝑛2) because you are checking all pairs in the array.
Space Complexity: 
𝑂(1) as it only requires constant space.
Disadvantages: The efficiency significantly drops as the array size increases.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                


"""
Solution 2: Sorting and Two-Pointer Method
This approach involves sorting the array and then using two pointers to find the two numbers that add up to the target. 
Note that this approach cannot be directly used to return the original indices unless additional steps are taken.

Steps:
Store each number with its original index as a tuple (value, index).
Sort these tuples by the number value.
Use two pointers, one starting at the beginning (left) and the other at the end (right).
If the sum of the two pointed numbers is greater than the target, move the right pointer leftward.
If the sum is less than the target, move the left pointer rightward.
If they match the target, return their original indices.

Time Complexity: 
𝑂(𝑛log⁡𝑛) due to the sorting step.
Space Complexity: 
𝑂(𝑛)for storing the tuple list.
Advantages: This method is simple and intuitive for scenarios where returning the indices isn't necessary.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_with_index = [(num, i) for i, num in enumerate(nums)]
        nums_with_index.sort()  # Sort by the values
        
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = nums_with_index[left][0] + nums_with_index[right][0]
            if current_sum == target:
                return [nums_with_index[left][1], nums_with_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1


"""
Solution 3: One-Pass Hash Map Method
This is a variation of the hash map approach where you check and store elements in the map during a single iteration over the array.

Steps:
Iterate through the array and compute the complement (target - nums[i]).
If the complement exists in the hash map, you have found the solution.
If not, store the current number and its index in the hash map.
This method is efficient and ensures you find the solution with a single pass through the array.

Time Complexity: 
𝑂(𝑛) due to a single pass through the array.
Space Complexity: 
𝑂(𝑛) for storing elements in the hash map.
Advantages: This method is highly efficient and commonly used due to its balance of time and space complexity.
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            seen[num] = i

        return seen
