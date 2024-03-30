class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        Finds the indices of two numbers in the input list that add up to the target value.

        Args:
            nums (List[int]): The list of integers.
            target (int): The target sum.

        Returns:
            List[int]: A list containing the indices of the two numbers that sum up to the 
            target.
        """
        
        # Dictionary to store previously seen numbers and their indices.
        prevMap = {}  # val -> index

        # Iterate through the list of numbers along with their indices.
        for i, n in enumerate(nums):
            # Calculate the difference needed to reach the target sum.
            diff = target - n
            # If the difference is found in the dictionary, return the two numbers' indices.
            if diff in prevMap:
                return [prevMap[diff], i]
            # Otherwise, store the current number and its index in the dictionary.
            prevMap[n] = i