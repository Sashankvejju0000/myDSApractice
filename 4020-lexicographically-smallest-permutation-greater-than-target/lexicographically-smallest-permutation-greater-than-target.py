class Solution(object):

    def lexGreaterPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """

        n = len(s)

        # Count characters in s
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        # save[i] = characters remaining after
        # matching target[0:i]
        save = [None] * n

        remaining = count[:]

        for i in range(n):

            # IMPORTANT:
            # Save BEFORE consuming target[i]
            save[i] = remaining[:]

            x = ord(target[i]) - ord('a')

            # Cannot match target[i]
            if remaining[x] == 0:
                break

            remaining[x] -= 1

        # Try the rightmost position first
        for i in range(n - 1, -1, -1):

            if save[i] is None:
                continue

            remaining = save[i][:]

            target_char = ord(target[i]) - ord('a')

            # Find smallest character > target[i]
            for c in range(target_char + 1, 26):

                if remaining[c] > 0:

                    # Prefix stays equal to target
                    ans = target[:i]

                    # Make it strictly greater
                    ans += chr(c + ord('a'))

                    remaining[c] -= 1

                    # Put remaining characters in sorted order
                    for j in range(26):
                        ans += chr(j + ord('a')) * remaining[j]

                    return ans

        return ""