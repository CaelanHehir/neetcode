class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""

        i = 0
        while all(i < len(string) for string in strs):
            if not len(set(string[i] for string in strs)) == 1:
                break
            res += strs[0][i]
            i += 1

        return res