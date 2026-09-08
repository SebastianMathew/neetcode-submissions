from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        b = ""
        for word in strs:
            b += str(len(word)) + "#" + word
        return b

    def decode(self, s: str) -> List[str]:
        o = []
        i = 0

        while i < len(s):
            j = i
            # Advance j until we hit the delimiter '#'
            while s[j] != "#":
                j += 1

            # Extract the full length (handles numbers > 9)
            length = int(s[i:j])

            # The word starts right after '#'
            start = j + 1
            end = start + length

            o.append(s[start:end])

            # Move pointer to the start of the next length string
            i = end

        return o