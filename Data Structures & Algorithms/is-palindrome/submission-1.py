class Solution:

    def cleanString(self, s: str) -> str:
        
        s = s.lower().strip()
        a = ord('a')
        z = ord('z')
        zero = ord('0')
        nine = ord('9')
        final_s = ""
        for char in s:
            # get bools
            is_alphabet = (ord(char) >= a and ord(char) <= z)
            is_numeric = (ord(char) >= zero and ord(char) <= nine)
            # check
            if is_alphabet or is_numeric:
                final_s += char
            else: 
                continue
        
        return final_s

    def isPalindrome(self, s: str) -> bool:
        
        s = self.cleanString(s)

        l, r = 0, len(s) - 1 

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return False
        
        return True