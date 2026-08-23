class Solution(object):
    def sumGame(self, num):

        n = len(num)
        mid = n // 2

        left_sum = 0
        right_sum = 0
        left_q = 0
        right_q = 0

        for i in range(mid):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        for i in range(mid, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Odd number of ? means Alice can force a win
        if (left_q + right_q) % 2 == 1:
            return True

        # Difference between number of ? on both sides
        q_diff = left_q - right_q

        # Maximum difference that can be created by '?' responses
        if left_sum - right_sum + (q_diff * 9) // 2 != 0:
            return True

        return False