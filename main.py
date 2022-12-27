# User function Template for python3

class Solution:
    ##Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    sum = 0
    def maxSubArraySum(self, arr, N):
            sum = 0
            max =arr[0]
            for i in range(0, N):
                sum=sum+arr[i]
                if max<sum:
                    max = sum
                if sum < 0:
                    sum = 0

            return max
obj=Solution()
print(obj.maxSubArraySum([-2, 1, -3, 4, -1, 2, 1, -5, 4],9))