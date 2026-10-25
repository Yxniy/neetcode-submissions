class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        subset = []

        def backtrack(start):
            # Every character has been partitioned
            if start == len(s):
                result.append(subset.copy())
                return

            # Try substrings of increasing length
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]

                # Only explore valid palindromes
                if substring == substring[::-1]:

                    subset.append(substring)

                    backtrack(end)

                    subset.pop()

        backtrack(0)
        return result