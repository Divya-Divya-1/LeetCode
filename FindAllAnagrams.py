from collections import Counter

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        len_p = len(p)
        len_s = len(s)
        if len_s < len_p:
            return res
        
        # Frequency of chars in p
        p_count = Counter(p)
        # Frequency of chars in the current window in s
        s_count = Counter()
        
        for i in range(len_s):
            # Add one char from the right side into the window
            s_count[s[i]] += 1
            
            # Remove one char from the left side when window size exceeds len_p
            if i >= len_p:
                left_char = s[i - len_p]
                s_count[left_char] -= 1
                if s_count[left_char] == 0:
                    del s_count[left_char]
            
            # Compare window with target
            if s_count == p_count:
                res.append(i - len_p + 1)
        
        return res
