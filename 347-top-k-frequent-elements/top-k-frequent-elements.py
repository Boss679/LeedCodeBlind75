class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in the given list of integers.

        Args:
            nums (List[int]): List of input integers.
            k (int): Number of most frequent elements to find.

        Returns:
            List[int]: List of k most frequent elements.
        """

        # Dictionary to store the frequency count of each element.
        count = {}

        # List of lists to store elements grouped by their frequency.
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each element in the input list.
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Group elements by their frequency.
        for n, c in count.items():
            freq[c].append(n)

        # List to store the result of k most frequent elements.
        res = []

        # Iterate over the frequency list in reverse order to get the most frequent elements first.
        for i in range(len(freq) - 1, 0, -1):
            # Iterate over elements with the same frequency.
            for n in freq[i]:
                res.append(n)
                # Check if we have found k elements.
                if len(res) == k:
                    return res