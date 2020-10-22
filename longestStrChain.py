'''
1048. Longest String Chain
Medium

956

61

Add to List

Share
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2.  For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.



Example 1:

Input: ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: one of the longest word chain is "a","ba","bda","bdca".


Note:

1 <= words.length <= 1000
1 <= words[i].length <= 16
words[i] only consists of English lowercase letters.
'''

class Solution:
    def longestStrChain(self, words):
        words.sort(key=len)
        dp = {}

        for word in words:
            for i in range(len(word)):
                if word not in dp:
                    dp[word] = dp.get(word[:i] + word[i + 1:], 0) + 1
                else:
                    dp[word] = max((dp.get(word[:i] + word[i + 1:], 0) + 1), dp[word])

        return max(dp.values())

if __name__ == '__main__':
    f = Solution()
    print(f.longestStrChain(["a","b","ba","bca","bda","bdca"]))