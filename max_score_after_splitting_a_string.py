class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        total_ones = s.count('1')  # Count total number of ones in the string
        max_score = 0
        left_zeros = 0
        left_ones = 0

        # Iterate through the string to find the maximum score
        for i in range(len(s) - 1):  # We stop at len(s) - 1 to ensure non-empty right substring
            if s[i] == '0':
                left_zeros += 1
            else:
                left_ones += 1

            # Calculate the score for the current split
            score = left_zeros + (total_ones - left_ones)
            max_score = max(max_score, score)

        return max_score
