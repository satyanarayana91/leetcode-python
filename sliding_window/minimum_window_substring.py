from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if not s or not t:
            return ""

        need = Counter(t)
        window = {}

        required = len(need)
        formed = 0

        left = 0

        best_length = float('inf')
        best_left = 0
        best_right = 0

        for right in range(len(s)):

            char = s[right]

            window[char] = window.get(char, 0) + 1

            if char in need and window[char] == need[char]:
                formed += 1

            while formed == required:

                current_length = right - left + 1

                if current_length < best_length:
                    best_length = current_length
                    best_left = left
                    best_right = right

                left_char = s[left]

                window[left_char] -= 1

                if (
                    left_char in need
                    and window[left_char] < need[left_char]
                ):
                    formed -= 1

                left += 1

        if best_length == float('inf'):
            return ""

        return s[best_left:best_right + 1]
