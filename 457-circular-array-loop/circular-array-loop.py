class Solution(object):
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)

        def next_index(i):
            return (i + nums[i]) % n

        for i in range(n):
            # Already processed
            if nums[i] == 0:
                continue

            direction = nums[i] > 0

            slow = i
            fast = i

            while True:
                # Move slow one step
                next_slow = next_index(slow)

                # Check direction of slow's next move
                if nums[next_slow] == 0 or (nums[next_slow] > 0) != direction:
                    break

                # Move fast one step
                next_fast = next_index(fast)

                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                # Move fast second step
                next_fast = next_index(next_fast)

                if nums[next_fast] == 0 or (nums[next_fast] > 0) != direction:
                    break

                slow = next_slow
                fast = next_fast

                if slow == fast:
                    # One-element cycle is invalid
                    if slow == next_index(slow):
                        break
                    return True

            # Mark this path as processed
            j = i
            while nums[j] != 0:
                next_j = next_index(j)

                # If next move changes direction, stop
                if (nums[j] > 0) != (nums[i] > 0):
                    break

                nums[j] = 0
                j = next_j

        return False