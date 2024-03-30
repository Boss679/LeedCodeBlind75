class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Determines if two input strings are anagrams of each other.

        Args:
            s (str): The first input string.
            t (str): The second input string.

        Returns:
            bool: True if the strings are anagrams, False otherwise.
        """
        
        if len(s) != len(t):
            return False

        # Create dictionaries to store the count of each character in both strings.
        countS, countT = {}, {}

        # Iterate through each character in the strings and update their counts in the  dictionaries.
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        
        # If the character counts in both dictionaries are equal, the strings are anagrams.
        return countS == countT