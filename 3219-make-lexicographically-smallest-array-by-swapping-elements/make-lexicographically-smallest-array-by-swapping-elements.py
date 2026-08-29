class Solution(object):

    def lexicographicallySmallestArray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: List[int]
        """

        n = len(nums)

        # Store (value, original_index)
        arr = []

        for i in range(n):
            arr.append((nums[i], i))

        # Sort by value
        arr.sort()

        ans = [0] * n

        i = 0

        while i < n:

            j = i

            # Find a group where consecutive values
            # differ by at most limit
            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
                j += 1

            # Values in this group can be freely rearranged
            values = []

            for k in range(i, j + 1):
                values.append(arr[k][0])

            # Original indices of this group
            indices = []

            for k in range(i, j + 1):
                indices.append(arr[k][1])

            # Put smallest values at smallest indices
            indices.sort()

            for k in range(len(values)):
                ans[indices[k]] = values[k]

            i = j + 1

        return ans