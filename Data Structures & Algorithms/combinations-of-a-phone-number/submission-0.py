class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []
        path = []
        if digits == "":
            return []
        def backtrack(i):

            if len(digits) == i:
                result.append("".join(path))
                return
            # Base case: all digits processed

            for j in mapping[digits[i]]:
                path.append(j)
                backtrack(i+1)
                path.pop()
            
        backtrack(0)
        return result

            # Loop through the letters for digits[i]
                # Choose a letter
                # Recurse to the next digit
                # Undo the choice