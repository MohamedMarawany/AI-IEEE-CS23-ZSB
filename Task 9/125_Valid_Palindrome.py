class Solution:
    def isPalindrome(self, s: str) -> bool:
        #str1 = s.lower()

        # Remove spaces, commas, and periods from the string
        #str1 = str1.replace(" ", "").replace(",", "").replace(".", "").replace(":", "")
        str1 = ''.join(ch for ch in s if ch.isalnum()).lower()

        # Check if the modified string is equal to its reverse
        return str1 == str1[::-1]