class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups anagrams together from the given list of strings.

        Args:
            strs (List[str]): List of input strings.

        Returns:
            List[List[str]]: A list of lists where each inner list contains anagrams of each other.
        """

        # Default dictionary to store anagrams grouped by their character counts.
        ans = collections.defaultdict(list)

        # Iterate through each string in the input list.
        for s in strs:
            # Initialize a count array to store the frequency of each character.
            count = [0] * 26
            # Count the occurrence of each character in the current string.
            for c in s:
                count[ord(c) - ord("a")] += 1
            # Convert the count array to a tuple and use it as a key in the defaultdict to group anagrams.
            ans[tuple(count)].append(s)
        
        # Return the values of the defaultdict, which are lists of grouped anagrams.
        return ans.values()